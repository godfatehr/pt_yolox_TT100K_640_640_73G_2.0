import os

# from yolox.exp import Exp as MyExp
from yolox.exp import ExpDeploy as MyExp

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.25
        self.input_size = (416, 416)
        self.mosaic_scale = (0.5, 1.5)
        # self.mosaic_prob = 0.2
        # self.mixup_prob = 0.2
        self.random_size = (10, 20)
        self.test_size = (416, 416)
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        self.enable_mixup = False

        # Define yourself dataset path
        self.data_dir = "datasets/data/"
        # self.train_ann = "train_small.json" # "train.json"
        # self.val_ann = "val_small.json" # "val.json" #"val.json"
        self.train_ann = "train.json"
        self.val_ann = "val.json"

        self.num_classes = 8

        self.max_epoch = 20 # 15
        self.data_num_workers = 4 #2
        self.eval_interval = 1
        self.no_aug_epochs = 3

        self.warmup_epochs = 2 # 1 # jwa

        # self.nmsthre = 0.