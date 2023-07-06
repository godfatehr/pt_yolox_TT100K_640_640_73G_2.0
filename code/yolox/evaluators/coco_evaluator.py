#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import contextlib
import io
import itertools
import json
import tempfile
import time
from collections import ChainMap, defaultdict
from loguru import logger
from tabulate import tabulate
from tqdm import tqdm

from pathlib import Path
import matplotlib.pyplot as plt

import numpy as np

import torch
import os

from tools.confusion_matrix import custom_evaluator, compute_conf_curves

from yolox.data.datasets import COCO_CLASSES
from yolox.utils import (
    gather,
    is_main_process,
    postprocess,
    synchronize,
    time_synchronized,
    xyxy2xywh,
    is_parallel,
    # xywh2xyxy,
)


def per_class_AR_table(coco_eval, class_names=COCO_CLASSES, headers=["class", "AR"], colums=6, iou05=False):
    per_class_AR = {}
    recalls = coco_eval.eval["recall"]
    # dimension of recalls: [TxKxAxM]
    # recall has dims (iou, cls, area range, max dets)
    assert len(class_names) == recalls.shape[1]

    for idx, name in enumerate(class_names):
        if not iou05:
            recall = recalls[:, idx, 0, -1]
        else:
            recall = recalls[0, idx, 0, -1]
        recall = recall[recall > -1]
        ar = np.mean(recall) if recall.size else float("nan") # compute mAP0.5:0.95
        per_class_AR[name] = float(ar * 100)

    num_cols = min(colums, len(per_class_AR) * len(headers))
    result_pair = [x for pair in per_class_AR.items() for x in pair]
    row_pair = itertools.zip_longest(*[result_pair[i::num_cols] for i in range(num_cols)])
    table_headers = headers * (num_cols // len(headers))
    table = tabulate(
        row_pair, tablefmt="pipe", floatfmt=".3f", headers=table_headers, numalign="left",
    )
    return table


def per_class_AP_table(coco_eval, class_names=COCO_CLASSES, headers=["class", "AP"], colums=6, iou05=False):
    per_class_AP = {}
    precisions = coco_eval.eval["precision"]
    # dimension of precisions: [TxRxKxAxM]
    # precision has dims (iou, recall, cls, area range, max dets)
    assert len(class_names) == precisions.shape[2]

    for idx, name in enumerate(class_names):
        # area range index 0: all area ranges
        # max dets index -1: typically 100 per image
        if not iou05:
            precision = precisions[:, :, idx, 0, -1]
        else:
            precision = precisions[0, :, idx, 0, -1]
        precision = precision[precision > -1]
        ap = np.mean(precision) if precision.size else float("nan")
        per_class_AP[name] = float(ap * 100)

    num_cols = min(colums, len(per_class_AP) * len(headers))
    result_pair = [x for pair in per_class_AP.items() for x in pair]
    row_pair = itertools.zip_longest(*[result_pair[i::num_cols] for i in range(num_cols)])
    table_headers = headers * (num_cols // len(headers))
    table = tabulate(
        row_pair, tablefmt="pipe", floatfmt=".3f", headers=table_headers, numalign="left",
    )
    return table

def plot_precision_recall_curves(coco_eval, save_dir='', class_names=COCO_CLASSES):
    all_precisions = coco_eval.eval["precision"]
    # dimension of precisions: [TxRxKxAxM]
    # precision has dims (iou, recall, cls, area range, max dets)
    # initialize figure
    fig = plt.figure(figsize=(10, 10))
    # iterate over all classes
    for class_idx in range(all_precisions.shape[2]):
        # get pr50 for this class
        pr50 = all_precisions[0, :, class_idx, 0, 2] # data for pr curve at iou=0.5, area=all, maxdets=100
        pr50 = pr50[pr50 > -1] # remove -1 values
        x = np.linspace(0, 1, len(pr50))
        plt.plot(x, pr50, label=class_names[class_idx])
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend()


    # creat folder 'plots' if not exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # check if file exist
    filename= os.path.join(save_dir, 'precision_recall_curve.png')
    if os.path.exists(filename):
        # if already exists find the next available number to append to the name
        i = 1
        while os.path.exists(filename):
            filename = os.path.join(save_dir, 'precision_recall_curve{}.png'.format(i))
            i += 1
    fig.savefig(filename, dpi=200)
    # save plot to file
    # fig.savefig(Path(save_dir) / 'precision_recall_curve.png', dpi=250)
    plt.close(fig)




class COCOEvaluator:
    """
    COCO AP Evaluation class.  All the data in the val2017 dataset are processed
    and evaluated by COCO API.
    """

    def __init__(
            self,
            dataloader,
            # val_loader = self.get_eval_loader(batch_size, is_distributed, testdev, legacy)
            # val_loader = torch.utils.data.DataLoader(valdataset, **dataloader_kwargs)
            # valdataset = COCODataset(
            #     data_dir=self.data_dir,
            #     json_file=self.val_ann if not testdev else self.test_ann,
            #     name="val2017" if not testdev else "test2017",
            #     img_size=self.test_size,
            #     preproc=ValTransform(legacy=legacy),
            # )
            img_size: int,
            confthre: float,
            nmsthre: float,
            num_classes: int,
            testdev: bool = False,
            per_class_AP: bool = True, #False, # jwa
            per_class_AR: bool = True, #False, # jwa
            exp_name: str = "yolox_nano",
            indepth_eval: bool = False,
    ):
        """
        Args:
            dataloader (Dataloader): evaluate dataloader.
            img_size: image size after preprocess. images are resized
                to squares whose shape is (img_size, img_size).
            confthre: confidence threshold ranging from 0 to 1, which
                is defined in the config file.
            nmsthre: IoU threshold of non-max supression ranging from 0 to 1.
            per_class_AP: Show per class AP during evalution or not. Default to False.
            per_class_AR: Show per class AR during evalution or not. Default to False.
        """
        self.dataloader = dataloader
        self.img_size = img_size
        self.confthre = confthre
        self.nmsthre = nmsthre
        self.num_classes = num_classes
        self.testdev = testdev
        self.per_class_AP = per_class_AP
        self.per_class_AR = per_class_AR
        self.exp_name = exp_name
        self.indepth_eval = indepth_eval
    def evaluate(
            self, model, distributed=False, half=False, trt_file=None,
            decoder=None, test_size=None, return_outputs=False
    ):
        """
        COCO average precision (AP) Evaluation. Iterate inference on the test dataset
        and the results are evaluated by COCO API.

        NOTE: This function will change training mode to False, please save states if needed.

        Args:
            model : model to evaluate.

        Returns:
            ap50_95 (float) : COCO AP of IoU=50:95
            ap50 (float) : COCO AP of IoU=50
            summary (sr): summary info of evaluation.
        """
        # TODO half to amp_test
        tensor_type = torch.cuda.HalfTensor if half else torch.cuda.FloatTensor
        model = model.eval()
        if half:
            model = model.half()
        ids = []
        data_list = []
        output_data = defaultdict()
        progress_bar = tqdm if is_main_process() else iter

        inference_time = 0
        nms_time = 0
        n_samples = max(len(self.dataloader) - 1, 1)

        if trt_file is not None:
            from torch2trt import TRTModule

            model_trt = TRTModule()
            model_trt.load_state_dict(torch.load(trt_file))

            x = torch.ones(1, 3, test_size[0], test_size[1]).cuda()
            model(x)
            model = model_trt

        for cur_iter, (imgs, _, info_imgs, ids) in enumerate(
                progress_bar(self.dataloader) # see code/yolox/data/datasets/coco.py for COCODataset
        ):
            ''' Returns:
            img (numpy.ndarray): pre-processed image
            padded_labels (torch.Tensor): pre-processed label data.
                The shape is :math:`[max_labels, 5]`.
                each label consists of [class, xc, yc, w, h]:
                    class (float): class index.
                    xc, yc (float) : center of bbox whose values range from 0 to 1.
                    w, h (float) : size of bbox whose values range from 0 to 1.
            info_img : tuple of h, w.
                h, w (int): original shape of the image
            img_id (int): same '''

            with torch.no_grad():
                imgs = imgs.type(tensor_type)

                # skip the last iters since batchsize might be not enough for batch inference
                is_time_record = cur_iter < len(self.dataloader) - 1
                if is_time_record:
                    start = time.time()

                outputs = model(imgs) # (batch_size, num_anchors, 5+num_classes) 5: x, y, w, h, obj_conf; num_classes: cls_conf1, cls_conf2, ...
                if is_parallel(model):
                    outputs = model.module.head.postprocess(outputs)
                else:
                    outputs = model.head.postprocess(outputs)
                if decoder is not None:
                    outputs = decoder(outputs, dtype=outputs.type())

                if is_time_record:
                    infer_end = time_synchronized()
                    inference_time += infer_end - start

                outputs = postprocess(
                    outputs, self.num_classes, self.confthre, self.nmsthre
                ) # shape: (batch_size, num_anchors, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred

                if is_time_record:
                    nms_end = time_synchronized()
                    nms_time += nms_end - infer_end

            data_list_elem, image_wise_data = self.convert_to_coco_format(
                outputs, info_imgs, ids, return_outputs=True)
            data_list.extend(data_list_elem)
            output_data.update(image_wise_data)

        statistics = torch.cuda.FloatTensor([inference_time, nms_time, n_samples])
        if distributed:
            data_list = gather(data_list, dst=0)
            output_data = gather(output_data, dst=0)
            data_list = list(itertools.chain(*data_list))
            output_data = dict(ChainMap(*output_data))
            torch.distributed.reduce(statistics, dst=0)

        eval_results = self.evaluate_prediction(data_list, statistics)
        synchronize()
        # if len(all_predictions) > 0:
        #     indepth_eval(all_targets, all_predictions)
        if return_outputs:
            return eval_results, output_data
        return eval_results

    def convert_to_coco_format(self, outputs, info_imgs, ids, return_outputs=False):
        # outputs: (batch_size, num_anchors, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred (bbox for 416x416)
        data_list = []
        image_wise_data = defaultdict(dict)
        for (output, img_h, img_w, img_id) in zip(
                outputs, info_imgs[0], info_imgs[1], ids
        ): # iterate over each image in the batch
            # outputs: (num_anchors, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred (bbox for 416x416)
            if output is None:
                continue
            output = output.cpu()

            bboxes = output[:, 0:4]

            # preprocessing: resize
            scale = min(
                self.img_size[0] / float(img_h), self.img_size[1] / float(img_w)
            )
            bboxes /= scale # scale back to original image size
            cls = output[:, 6]
            scores = output[:, 4] * output[:, 5]

            image_wise_data.update({
                int(img_id): {
                    "bboxes": [box.numpy().tolist() for box in bboxes], # (num_boxes, 4)
                    "scores": [score.numpy().item() for score in scores], # (num_boxes, ): score of each box: obj_conf * cls_conf
                    "categories": [ # (num_boxes, ): category of each box: cls_pred
                        self.dataloader.dataset.class_ids[int(cls[ind])]
                        for ind in range(bboxes.shape[0])
                    ],
                }
            })

            bboxes = xyxy2xywh(bboxes)

            for ind in range(bboxes.shape[0]): # for each bbox
                label = self.dataloader.dataset.class_ids[int(cls[ind])] # get label
                pred_data = {
                    "image_id": int(img_id), # image id
                    "category_id": label, # label
                    "bbox": bboxes[ind].numpy().tolist(), # bbox: x, y, w, h
                    "score": scores[ind].numpy().item(), # score: obj_conf * cls_conf
                    "segmentation": [],
                }  # COCO json format
                data_list.append(pred_data)

        if return_outputs:
            return data_list, image_wise_data
        return data_list

    def evaluate_prediction(self, data_dict, statistics): # data_dict: list of dict, each dict is a bbox
        if not is_main_process():
            return 0, 0, None

        logger.info("Evaluate in main process...")

        annType = ["segm", "bbox", "keypoints"]

        inference_time = statistics[0].item()
        nms_time = statistics[1].item()
        n_samples = statistics[2].item()

        a_infer_time = 1000 * inference_time / (n_samples * self.dataloader.batch_size)
        a_nms_time = 1000 * nms_time / (n_samples * self.dataloader.batch_size)

        time_info = ", ".join(
            [
                "Average {} time: {:.2f} ms".format(k, v)
                for k, v in zip(
                ["forward", "NMS", "inference"],
                [a_infer_time, a_nms_time, (a_infer_time + a_nms_time)],
            )
            ]
        )

        info = time_info + "\n"

        # Evaluate the Dt (detection) json comparing with the ground truth
        if len(data_dict) > 0:
            cocoGt = self.dataloader.dataset.coco # load ground truth annotations; cocoGt: COCO object
            # TODO: since pycocotools can't process dict in py36, write data to json file.
            if self.testdev:
                json.dump(data_dict, open("./yolox_testdev_2017.json", "w"))
                cocoDt = cocoGt.loadRes("./yolox_testdev_2017.json")
            else:
                _, tmp = tempfile.mkstemp()
                json.dump(data_dict, open(tmp, "w"))
                cocoDt = cocoGt.loadRes(tmp) # load detection results
            try:
                from yolox.layers import COCOeval_opt as COCOeval
            except ImportError:
                from pycocotools.cocoeval import COCOeval
                logger.warning("Use standard COCOeval.")
            # from pycocotools.cocoeval import COCOeval
            logger.warning("Use standard COCOeval.")

            cocoEval = COCOeval(cocoGt, cocoDt, annType[1])
            cocoEval.evaluate()
            cocoEval.accumulate()

            # jwa
            cat_ids = list(cocoGt.cats.keys())
            cat_names = [cocoGt.cats[catId]['name'] for catId in sorted(cat_ids)]

            if self.indepth_eval:
                print('indepth_eval')
                plot_precision_recall_curves(cocoEval, save_dir=os.path.join(os.getcwd(), 'YOLOX_outputs', self.exp_name, 'plots', 'val'), class_names=cat_names)
                compute_conf_curves(cocoEval, save_dir=os.path.join(os.getcwd(), 'YOLOX_outputs', self.exp_name, 'plots', 'val'))

            redirect_string = io.StringIO()
            with contextlib.redirect_stdout(redirect_string):
                cocoEval.summarize()
            info += redirect_string.getvalue()
            cat_ids = list(cocoGt.cats.keys())
            cat_names = [cocoGt.cats[catId]['name'] for catId in sorted(cat_ids)]
            if self.per_class_AP:
                AP_table = per_class_AP_table(cocoEval, class_names=cat_names)
                info += "per class AP50:95:\n" + AP_table + "\n"
                AP_table = per_class_AP_table(cocoEval, class_names=cat_names, iou05=True, headers=["class", "AP50"])
                info += "per class AP50:\n" + AP_table + "\n"
            if self.per_class_AR: # Recall
                AR_table = per_class_AR_table(cocoEval, class_names=cat_names)
                info += "per class AR50:95:\n" + AR_table + "\n"
                AR_table = per_class_AR_table(cocoEval, class_names=cat_names, iou05=True, headers=["class", "AR50"])
                info += "per class AR50:\n" + AR_table + "\n"
            # plot confusion matrix
            # get_confusion_matrix(cocoEval)
            return cocoEval.stats[0], cocoEval.stats[1], info
        else:
            return 0, 0, info

