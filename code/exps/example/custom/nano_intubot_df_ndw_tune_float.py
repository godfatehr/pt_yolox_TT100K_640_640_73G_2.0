import os

# from yolox.exp import Exp as MyExp
from yolox.exp import ExpDeploy as MyExp

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.25
        self.input_size = (416, 416)
        self.test_size = (416, 416)
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/data/"
        # self.train_ann = "train_small.json" # "train.json"
        # self.val_ann = "val_small.json" # "val.json" #"val.json"
        self.train_ann = "train.json"
        self.val_ann = "val.json"

        self.num_classes = 8

        self.max_epoch = 10 # 15
        self.warmup_epochs = 2        
        self.data_num_workers = 4
        self.eval_interval = 1
        self.no_aug_epochs = 2
        self.basic_lr_per_img = 0.005 / 64.0 # 0.01 / 64.0

        # --------------- transform config ----------------- #
        self.random_size = (10, 20)
        # self.multiscale_range = 0.
        self.mosaic_prob = 0.0 #1.0
        self.mixup_prob = 0.0 #1.0
        self.hsv_prob = 1.0 #1.0
        self.flip_prob = 0.5 #0.5
        self.degrees = 10.0 #10.0
        self.translate = 0.1 #0.1
        self.mosaic_scale = (0.8,1.75) #(.7, 2.0) # random resize scale
        self.mixup_scale = (0.5, 1.5)
        self.shear = 2.0 #2.0
        self.enable_mixup = False #True
        self.blur_prob = 0.5 #0.5