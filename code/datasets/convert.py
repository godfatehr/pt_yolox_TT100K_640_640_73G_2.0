# Copyright 2019 Xilinx Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pdb
import json
import cv2
from tqdm import tqdm
import os
import argparse
import datetime


cat_names = ['i2', 'i4', 'i5', 'il100', 'il60', 'il80', 'io', 'ip', 'p10', 'p11',
              'p12', 'p19', 'p23', 'p26', 'p27', 'p3', 'p5', 'p6', 'pg', 'ph4',
              'ph4.5', 'ph5', 'pl100', 'pl120', 'pl20', 'pl30', 'pl40', 'pl5', 'pl50', 'pl60',
              'pl70', 'pl80', 'pm20', 'pm30', 'pm55', 'pn', 'pne', 'po', 'pr40', 'w13',
              'w32', 'w55', 'w57', 'w59', 'wo']


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def splitTT100_and_convert(json_dataset):
    with open(json_dataset,'r') as f:
        dataset = json.load(f)
        for keys in tqdm(dataset['imgs']):
            path = dataset['imgs'][keys]['path']
            image_type = path.split('/')[0]
            image_ids = path.split('/')[-1].split('.')[0]
            if image_type in ['train','test']:
                label_txt = open(image_type +'/' +image_ids+'.txt','w')
                img = cv2.imread(path)
                w = int(img.shape[1])
                h = int(img.shape[0])
                objects = dataset['imgs'][keys]['objects']
                if objects is None:
                    continue
                else:
                    for num in range(len(objects)):
                        category = objects[num]['category']
                        if category in cat_names:
                            cls_id = cat_names.index(category)
                            xmin = objects[num]['bbox']['xmin']
                            xmax = objects[num]['bbox']['xmax']
                            ymin = objects[num]['bbox']['ymin']
                            ymax = objects[num]['bbox']['ymax']
                            b = (float(xmin),float(xmax),float(ymin),float(ymax))
                            bb = convert((w,h), b)
                            label_txt.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

class TT100KCOCOConverter():
    def __init__(self,
                image_dir,
                image_prefix="",
                txt_prefix=""):

        self.image_dir = image_dir
        self.image_prefix = image_prefix
        self.txt_prefix = txt_prefix

        self.init_coco_format_info()

        self.img_index = 0
        self.annotation_index = 0
        self.img_dicts = []
        self.annotation_dicts = []

    def init_coco_format_info(self):
        self.dataset_info = {
            "year": 2020,
            "version": "v1.0",
            "description": "TT100K Dataset 2D Detection",
            "contributor": "Tsinghua LLC",
            "url": "",
            "date_created": datetime.datetime.utcnow().isoformat(' '),
        }
        self.licenses = [{
            "id": 1,
            "name": "TT100K Dataset License Agreement for Non-Commercial Use",
            "url": "",
        }]

        self.target_categories = [
            {
                "id": idx+1,
                "name": x,
                "supercategory": x
            }
            for idx, x in enumerate(cat_names)
        ]
    
    def process_images(self, imgpath_list):
        for imgpath in tqdm(imgpath_list):
            img = cv2.imread(os.path.join(self.image_prefix, imgpath))
            img_name = imgpath.split(".")[0]
            label_path = os.path.join(self.txt_prefix, img_name + ".txt")
            # import ipdb; ipdb.set_trace()

            try:
                height, width, _ = img.shape
            except:
                print('no image: ', os.path.join(self.image_prefix, imgpath))
                continue
            self.add_coco_img_dict(imgpath, height=height, width=width)

            try:
                with open(label_path, 'r') as f:
                    img_txt = f.readlines()
                    img_txt = [x.strip() for x in img_txt]
            except:
                print('no label: ', os.path.join(label_path))
                continue
            self.add_coco_annotation_dict(img_txt, width, height)
            self.img_index += 1
    
    def add_coco_img_dict(self,
                          file_name,
                          height=None,
                          width=None):
        if height is None or width is None:
            raise ValueError

        img_dict = {
            'id': self.img_index,
            'width': width,
            'height': height,
            'file_name': file_name,
            'license': 1,
        }
        
        self.img_dicts.append(img_dict)

    def add_coco_annotation_dict(self,
                                 img_txt,
                                 img_width,
                                 img_height):
        annotation_dicts = []
        for box_label in img_txt:
            label_splits = box_label.split(" ")
            category_id = int(label_splits[0]) + 1
            width = float(label_splits[3]) * img_width # box.length: dim x
            height = float(label_splits[4]) * img_height # box.width: dim y
            x1 = float(label_splits[1]) * img_width - width / 2
            y1 = float(label_splits[2]) * img_height - height / 2
            
            annotation_dict = {
                "id": self.annotation_index,
                "image_id": self.img_index,
                "category_id": category_id,
                "segmentation": None,
                "area": width * height,
                "bbox": [x1, y1, width, height],
                "iscrowd": 0,
            }
            annotation_dicts.append(annotation_dict)
            self.annotation_index += 1
        self.annotation_dicts.extend(annotation_dicts)

    def write_coco(self, label_path, json_indent=None):
        output_dict = {
            "info": self.dataset_info,
            "licenses": self.licenses,
            "categories": self.target_categories,
            "images": self.img_dicts,
        }
        if self.annotation_dicts:
            output_dict["annotations"] = self.annotation_dicts

        with open(label_path, mode='w') as f:
            # dump with a trick for rounding float
            json.dump(json.loads(json.dumps(output_dict),
                                 parse_float=lambda x: round(float(x), 6)),
                      f,
                      indent=json_indent,
                      sort_keys=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--work_dir', default='.', type=str)
    #parser.add_argument('--image_dirname', required=True, type=str)
    #parser.add_argument('--image_filename_prefix', default=None, type=str, help="used to complement the image path during readin")
    #parser.add_argument('--txt_filename_prefix', default=None, type=str, help="used to complement the label path during readin")
    parser.add_argument('--label_dirname', default='annotations', type=str, help="output dir name")
    parser.add_argument('--gt_json_filename', required=True, type=str, help="gt filename")
    args = parser.parse_args()

    print("Start Split the dataset and Convert to yolo")
    splitTT100_and_convert(args.gt_json_filename)
    
    for dataset_type in ['train','test']:
        image_dirname = dataset_type
        label_filename = 'tt100k_in_coco_format_' + dataset_type + '.json'
        image_filename_prefix=dataset_type
        txt_filename_prefix=dataset_type
        image_dir = os.path.join(args.work_dir, image_dirname)
        label_dir = os.path.join(args.work_dir, args.label_dirname)
        os.makedirs(label_dir, exist_ok=True)
        label_path = os.path.join(label_dir, label_filename)
    
        imgpaths = os.listdir(image_dir)
        imgpath_list = [x for x in imgpaths if x.endswith(('.jpeg', '.png', '.jpg'))]
    
        print("Convert dataset tt100k to coco format for yolox")
        converter = TT100KCOCOConverter(
            image_dir,
            image_filename_prefix,
            txt_filename_prefix
        )
        converter.process_images(imgpath_list)
        converter.write_coco(label_path)

def test(anno_path):
    from pycocotools.coco import COCO
    from pycocotools.cocoeval import COCOeval

    with open(anno_path, 'r') as f:
        annotations = json.load(f)
    import ipdb; ipdb.set_trace()
    cocoGt = COCO(anno_path)

if __name__ == "__main__":
    main()
    # test('annotations/tt100k_in_coco_format_train.json')
