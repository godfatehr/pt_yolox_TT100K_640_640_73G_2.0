#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii Inc. All rights reserved.

import numpy as np

import torch
import torchvision

__all__ = [
    "filter_box",
    "postprocess",
    "bboxes_iou",
    "matrix_iou",
    "adjust_box_anns",
    "xyxy2xywh",
    "xyxy2cxcywh",
]


def filter_box(output, scale_range):
    """
    output: (N, 5+class) shape
    """
    min_scale, max_scale = scale_range
    w = output[:, 2] - output[:, 0]
    h = output[:, 3] - output[:, 1]
    keep = (w * h > min_scale * min_scale) & (w * h < max_scale * max_scale)
    return output[keep]

def get_best_dets_per_class(detections_tensor):
    max_scores, max_score_indices = [], []
    for class_id in range(int(torch.max(detections_tensor[:, 6]).item()) + 1):
        # get indices of the elements with the current class_id
        indices = torch.nonzero(detections_tensor[:, 6] == class_id).squeeze(1)
        if indices.numel() > 0:  # if there are elements with the current class_id
            # compute the scores as the product of the first and second elements
            scores = detections_tensor[indices, 4] * detections_tensor[indices, 5]
            # get the maximum score and its index along the current class_id's elements
            max_score, max_score_index = torch.max(scores, dim=0)
            # store the maximum score and its index
            max_scores.append(max_score.item())
            max_score_indices.append(indices[max_score_index].item())
    return max_score_indices

def postprocess(prediction, num_classes, conf_thre=0.7, nms_thre=0.45, class_agnostic=False):
    box_corner = prediction.new(prediction.shape) # (batch_size, num_anchors, 5+num_classes) 5: x, y, w, h, obj_conf; num_classes: cls_conf1, cls_conf2, ...
    box_corner[:, :, 0] = prediction[:, :, 0] - prediction[:, :, 2] / 2
    box_corner[:, :, 1] = prediction[:, :, 1] - prediction[:, :, 3] / 2
    box_corner[:, :, 2] = prediction[:, :, 0] + prediction[:, :, 2] / 2
    box_corner[:, :, 3] = prediction[:, :, 1] + prediction[:, :, 3] / 2
    prediction[:, :, :4] = box_corner[:, :, :4] # convert xywh to xyxy

    output = [None for _ in range(len(prediction))]
    for i, image_pred in enumerate(prediction): # iterate over each image in batch

        # If none are remaining => process next image
        if not image_pred.size(0):
            continue
        # Get score and class index with highest confidence for each box
        class_conf, class_pred = torch.max(image_pred[:, 5: 5 + num_classes], 1, keepdim=True) # dim=1: max along each row; keepdim=True: get index of max value

        conf_mask = (image_pred[:, 4] * class_conf.squeeze() >= conf_thre).squeeze() # obj_conf * cls_conf = pred_conf >= conf_thre
        # Detections ordered as (x1, y1, x2, y2, obj_conf, class_conf, class_pred)
        detections = torch.cat((image_pred[:, :5], class_conf, class_pred.float()), 1)
        detections = detections[conf_mask] # filter out detections with low confidence (below conf_thre)
        # detections shape: (num_detections, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred
        if not detections.size(0):
            continue

        best_dets_per_class = get_best_dets_per_class(detections)

        detections = detections[best_dets_per_class] # select elements that have been kept by nms
        # detections shape: (num_detections, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred
        if output[i] is None:
            output[i] = detections
        else:
            output[i] = torch.cat((output[i], detections))

    return output     


# def postprocess(prediction, num_classes, conf_thre=0.7, nms_thre=0.45, class_agnostic=False):
#     box_corner = prediction.new(prediction.shape) # (batch_size, num_anchors, 5+num_classes) 5: x, y, w, h, obj_conf; num_classes: cls_conf1, cls_conf2, ...
#     box_corner[:, :, 0] = prediction[:, :, 0] - prediction[:, :, 2] / 2
#     box_corner[:, :, 1] = prediction[:, :, 1] - prediction[:, :, 3] / 2
#     box_corner[:, :, 2] = prediction[:, :, 0] + prediction[:, :, 2] / 2
#     box_corner[:, :, 3] = prediction[:, :, 1] + prediction[:, :, 3] / 2
#     prediction[:, :, :4] = box_corner[:, :, :4] # convert xywh to xyxy

#     output = [None for _ in range(len(prediction))]
#     for i, image_pred in enumerate(prediction): # iterate over each image in batch

#         # If none are remaining => process next image
#         if not image_pred.size(0):
#             continue
#         # Get score and class index with highest confidence for each box
#         class_conf, class_pred = torch.max(image_pred[:, 5: 5 + num_classes], 1, keepdim=True) # dim=1: max along each row; keepdim=True: get index of max value

#         conf_mask = (image_pred[:, 4] * class_conf.squeeze() >= conf_thre).squeeze() # obj_conf * cls_conf = pred_conf >= conf_thre
#         # Detections ordered as (x1, y1, x2, y2, obj_conf, class_conf, class_pred)
#         detections = torch.cat((image_pred[:, :5], class_conf, class_pred.float()), 1)
#         detections = detections[conf_mask] # filter out detections with low confidence (below conf_thre)
#         # detections shape: (num_detections, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred
#         if not detections.size(0):
#             continue
#         # perform nms
#         if class_agnostic:
#             nms_out_index = torchvision.ops.nms(
#                 detections[:, :4],
#                 detections[:, 4] * detections[:, 5],
#                 nms_thre,
#                 )
#         else: # nms for each class
#             nms_out_index = torchvision.ops.batched_nms(
#                 detections[:, :4], # xyxy
#                 detections[:, 4] * detections[:, 5], # obj_conf * cls_conf
#                 detections[:, 6], # class_pred
#                 nms_thre, # nms_thre
#             )

#         detections = detections[nms_out_index] # select elements that have been kept by nms
#         # detections shape: (num_detections, 7) 7: x1, y1, x2, y2, obj_conf, cls_conf, cls_pred
#         if output[i] is None:
#             output[i] = detections
#         else:
#             output[i] = torch.cat((output[i], detections))

#     return output


def bboxes_iou(bboxes_a, bboxes_b, xyxy=True):
    if bboxes_a.shape[1] != 4 or bboxes_b.shape[1] != 4:
        raise IndexError

    if xyxy:
        tl = torch.max(bboxes_a[:, None, :2], bboxes_b[:, :2])
        br = torch.min(bboxes_a[:, None, 2:], bboxes_b[:, 2:])
        area_a = torch.prod(bboxes_a[:, 2:] - bboxes_a[:, :2], 1)
        area_b = torch.prod(bboxes_b[:, 2:] - bboxes_b[:, :2], 1)
    else:
        tl = torch.max(
            (bboxes_a[:, None, :2] - bboxes_a[:, None, 2:] / 2),
            (bboxes_b[:, :2] - bboxes_b[:, 2:] / 2),
        )
        br = torch.min(
            (bboxes_a[:, None, :2] + bboxes_a[:, None, 2:] / 2),
            (bboxes_b[:, :2] + bboxes_b[:, 2:] / 2),
        )

        area_a = torch.prod(bboxes_a[:, 2:], 1)
        area_b = torch.prod(bboxes_b[:, 2:], 1)
    en = (tl < br).type(tl.type()).prod(dim=2)
    area_i = torch.prod(br - tl, 2) * en  # * ((tl < br).all())
    return area_i / (area_a[:, None] + area_b - area_i)


def matrix_iou(a, b):
    """
    return iou of a and b, numpy version for data augenmentation
    """
    lt = np.maximum(a[:, np.newaxis, :2], b[:, :2])
    rb = np.minimum(a[:, np.newaxis, 2:], b[:, 2:])

    area_i = np.prod(rb - lt, axis=2) * (lt < rb).all(axis=2)
    area_a = np.prod(a[:, 2:] - a[:, :2], axis=1)
    area_b = np.prod(b[:, 2:] - b[:, :2], axis=1)
    return area_i / (area_a[:, np.newaxis] + area_b - area_i + 1e-12)


def adjust_box_anns(bbox, scale_ratio, padw, padh, w_max, h_max):
    bbox[:, 0::2] = np.clip(bbox[:, 0::2] * scale_ratio + padw, 0, w_max)
    bbox[:, 1::2] = np.clip(bbox[:, 1::2] * scale_ratio + padh, 0, h_max)
    return bbox


def xyxy2xywh(bboxes):
    bboxes[:, 2] = bboxes[:, 2] - bboxes[:, 0]
    bboxes[:, 3] = bboxes[:, 3] - bboxes[:, 1]
    return bboxes


def xyxy2cxcywh(bboxes):
    bboxes[:, 2] = bboxes[:, 2] - bboxes[:, 0]
    bboxes[:, 3] = bboxes[:, 3] - bboxes[:, 1]
    bboxes[:, 0] = bboxes[:, 0] + bboxes[:, 2] * 0.5
    bboxes[:, 1] = bboxes[:, 1] + bboxes[:, 3] * 0.5
    return bboxes

# def xywh2xyxy(x):
#     # Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
#     y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
#     y[..., 0] = x[..., 0] - x[..., 2] / 2  # top left x
#     y[..., 1] = x[..., 1] - x[..., 3] / 2  # top left y
#     y[..., 2] = x[..., 0] + x[..., 2] / 2  # bottom right x
#     y[..., 3] = x[..., 1] + x[..., 3] / 2  # bottom right y
#     return y
#
# def xywhn2xyxy(x, w=640, h=640, padw=0, padh=0):
#     # Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
#     y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
#     y[..., 0] = w * (x[..., 0] - x[..., 2] / 2) + padw  # top left x
#     y[..., 1] = h * (x[..., 1] - x[..., 3] / 2) + padh  # top left y
#     y[..., 2] = w * (x[..., 0] + x[..., 2] / 2) + padw  # bottom right x
#     y[..., 3] = h * (x[..., 1] + x[..., 3] / 2) + padh  # bottom right y
#     return y