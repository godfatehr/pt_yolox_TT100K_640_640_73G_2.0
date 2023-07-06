# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class YOLOX(torch.nn.Module):
    def __init__(self):
        super(YOLOX, self).__init__()
        self.module_0 = py_nndct.nn.Input() #YOLOX::input_0
        self.module_1 = py_nndct.nn.quant_input() #YOLOX::YOLOX/QuantStub[quant_in]/input.1
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=48, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/FocusDeploy[stem]/BaseConv[conv]/Conv2d[conv]/input.2
        self.module_4 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/FocusDeploy[stem]/BaseConv[conv]/LeakyReLU[act]/input.4
        self.module_5 = py_nndct.nn.Conv2d(in_channels=48, out_channels=96, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/BaseConv[0]/Conv2d[conv]/input.5
        self.module_7 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/BaseConv[0]/LeakyReLU[act]/input.7
        self.module_8 = py_nndct.nn.Conv2d(in_channels=96, out_channels=48, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.8
        self.module_10 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv1]/LeakyReLU[act]/input.12
        self.module_11 = py_nndct.nn.Conv2d(in_channels=96, out_channels=48, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.10
        self.module_13 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv2]/LeakyReLU[act]/21953
        self.module_14 = py_nndct.nn.Conv2d(in_channels=48, out_channels=48, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.13
        self.module_16 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.15
        self.module_17 = py_nndct.nn.Conv2d(in_channels=48, out_channels=48, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.16
        self.module_19 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/22007
        self.module_20 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/Add[sc_add]/input.18
        self.module_21 = py_nndct.nn.Conv2d(in_channels=48, out_channels=48, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.19
        self.module_23 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.21
        self.module_24 = py_nndct.nn.Conv2d(in_channels=48, out_channels=48, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.22
        self.module_26 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/22063
        self.module_27 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/Add[sc_add]/22065
        self.module_28 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Cat[cat]/input.24
        self.module_29 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.25
        self.module_31 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv3]/LeakyReLU[act]/input.27
        self.module_32 = py_nndct.nn.Conv2d(in_channels=96, out_channels=192, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/BaseConv[0]/Conv2d[conv]/input.28
        self.module_34 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/BaseConv[0]/LeakyReLU[act]/input.30
        self.module_35 = py_nndct.nn.Conv2d(in_channels=192, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.31
        self.module_37 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv1]/LeakyReLU[act]/input.35
        self.module_38 = py_nndct.nn.Conv2d(in_channels=192, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.33
        self.module_40 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv2]/LeakyReLU[act]/22176
        self.module_41 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.36
        self.module_43 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.38
        self.module_44 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.39
        self.module_46 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/22230
        self.module_47 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/Add[sc_add]/input.41
        self.module_48 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.42
        self.module_50 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.44
        self.module_51 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.45
        self.module_53 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/22286
        self.module_54 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/Add[sc_add]/input.47
        self.module_55 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.48
        self.module_57 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/LeakyReLU[act]/input.50
        self.module_58 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv2]/Conv2d[conv]/input.51
        self.module_60 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv2]/LeakyReLU[act]/22342
        self.module_61 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/Add[sc_add]/input.53
        self.module_62 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv1]/Conv2d[conv]/input.54
        self.module_64 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv1]/LeakyReLU[act]/input.56
        self.module_65 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv2]/Conv2d[conv]/input.57
        self.module_67 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv2]/LeakyReLU[act]/22398
        self.module_68 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/Add[sc_add]/input.59
        self.module_69 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv1]/Conv2d[conv]/input.60
        self.module_71 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv1]/LeakyReLU[act]/input.62
        self.module_72 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv2]/Conv2d[conv]/input.63
        self.module_74 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv2]/LeakyReLU[act]/22454
        self.module_75 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/Add[sc_add]/input.65
        self.module_76 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv1]/Conv2d[conv]/input.66
        self.module_78 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv1]/LeakyReLU[act]/input.68
        self.module_79 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv2]/Conv2d[conv]/input.69
        self.module_81 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv2]/LeakyReLU[act]/22510
        self.module_82 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/Add[sc_add]/22512
        self.module_83 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Cat[cat]/input.71
        self.module_84 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.72
        self.module_86 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv3]/LeakyReLU[act]/input.74
        self.module_87 = py_nndct.nn.Conv2d(in_channels=192, out_channels=384, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/BaseConv[0]/Conv2d[conv]/input.75
        self.module_89 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/BaseConv[0]/LeakyReLU[act]/input.77
        self.module_90 = py_nndct.nn.Conv2d(in_channels=384, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.78
        self.module_92 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv1]/LeakyReLU[act]/input.82
        self.module_93 = py_nndct.nn.Conv2d(in_channels=384, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.80
        self.module_95 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv2]/LeakyReLU[act]/22623
        self.module_96 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.83
        self.module_98 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.85
        self.module_99 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.86
        self.module_101 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/22677
        self.module_102 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/Add[sc_add]/input.88
        self.module_103 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.89
        self.module_105 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.91
        self.module_106 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.92
        self.module_108 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/22733
        self.module_109 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/Add[sc_add]/input.94
        self.module_110 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.95
        self.module_112 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/LeakyReLU[act]/input.97
        self.module_113 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv2]/Conv2d[conv]/input.98
        self.module_115 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv2]/LeakyReLU[act]/22789
        self.module_116 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/Add[sc_add]/input.100
        self.module_117 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv1]/Conv2d[conv]/input.101
        self.module_119 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv1]/LeakyReLU[act]/input.103
        self.module_120 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv2]/Conv2d[conv]/input.104
        self.module_122 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/BaseConv[conv2]/LeakyReLU[act]/22845
        self.module_123 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[3]/Add[sc_add]/input.106
        self.module_124 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv1]/Conv2d[conv]/input.107
        self.module_126 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv1]/LeakyReLU[act]/input.109
        self.module_127 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv2]/Conv2d[conv]/input.110
        self.module_129 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/BaseConv[conv2]/LeakyReLU[act]/22901
        self.module_130 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[4]/Add[sc_add]/input.112
        self.module_131 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv1]/Conv2d[conv]/input.113
        self.module_133 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv1]/LeakyReLU[act]/input.115
        self.module_134 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv2]/Conv2d[conv]/input.116
        self.module_136 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/BaseConv[conv2]/LeakyReLU[act]/22957
        self.module_137 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[5]/Add[sc_add]/22959
        self.module_138 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Cat[cat]/input.118
        self.module_139 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.119
        self.module_141 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv3]/LeakyReLU[act]/input.121
        self.module_142 = py_nndct.nn.Conv2d(in_channels=384, out_channels=768, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/BaseConv[0]/Conv2d[conv]/input.122
        self.module_144 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/BaseConv[0]/LeakyReLU[act]/input.124
        self.module_145 = py_nndct.nn.Conv2d(in_channels=768, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.125
        self.module_147 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/23043
        self.module_148 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/MaxPool2d[m]/ModuleList[0]/23057
        self.module_149 = py_nndct.nn.MaxPool2d(kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/MaxPool2d[m]/ModuleList[1]/23071
        self.module_150 = py_nndct.nn.MaxPool2d(kernel_size=[7, 7], stride=[1, 1], padding=[3, 3], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/MaxPool2d[m]/ModuleList[2]/23085
        self.module_151 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/Cat[cat]/input.127
        self.module_152 = py_nndct.nn.Conv2d(in_channels=1536, out_channels=768, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.128
        self.module_154 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/input.130
        self.module_155 = py_nndct.nn.Conv2d(in_channels=768, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv1]/Conv2d[conv]/input.131
        self.module_157 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv1]/LeakyReLU[act]/input.135
        self.module_158 = py_nndct.nn.Conv2d(in_channels=768, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv2]/Conv2d[conv]/input.133
        self.module_160 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv2]/LeakyReLU[act]/23169
        self.module_161 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.136
        self.module_163 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.138
        self.module_164 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.139
        self.module_166 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/input.141
        self.module_167 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.142
        self.module_169 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.144
        self.module_170 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.145
        self.module_172 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/23277
        self.module_173 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Cat[cat]/input.147
        self.module_174 = py_nndct.nn.Conv2d(in_channels=768, out_channels=768, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv3]/Conv2d[conv]/input.148
        self.module_176 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv3]/LeakyReLU[act]/input.150
        self.module_177 = py_nndct.nn.Conv2d(in_channels=768, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[lateral_conv0]/Conv2d[conv]/input.151
        self.module_179 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[lateral_conv0]/LeakyReLU[act]/input.153
        self.module_180 = py_nndct.nn.Interpolate() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Upsample[upsample]/23343
        self.module_181 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_f0]/input.154
        self.module_182 = py_nndct.nn.Conv2d(in_channels=768, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv1]/Conv2d[conv]/input.155
        self.module_184 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv1]/LeakyReLU[act]/input.159
        self.module_185 = py_nndct.nn.Conv2d(in_channels=768, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv2]/Conv2d[conv]/input.157
        self.module_187 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv2]/LeakyReLU[act]/23400
        self.module_188 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.160
        self.module_190 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.162
        self.module_191 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.163
        self.module_193 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/input.165
        self.module_194 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.166
        self.module_196 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.168
        self.module_197 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.169
        self.module_199 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/23508
        self.module_200 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Cat[cat]/input.171
        self.module_201 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv3]/Conv2d[conv]/input.172
        self.module_203 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv3]/LeakyReLU[act]/input.174
        self.module_204 = py_nndct.nn.Conv2d(in_channels=384, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[reduce_conv1]/Conv2d[conv]/input.175
        self.module_206 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[reduce_conv1]/LeakyReLU[act]/input.177
        self.module_207 = py_nndct.nn.Interpolate() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Upsample[upsample]/23570
        self.module_208 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_f1]/input.178
        self.module_209 = py_nndct.nn.Conv2d(in_channels=384, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv1]/Conv2d[conv]/input.179
        self.module_211 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv1]/LeakyReLU[act]/input.183
        self.module_212 = py_nndct.nn.Conv2d(in_channels=384, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv2]/Conv2d[conv]/input.181
        self.module_214 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv2]/LeakyReLU[act]/23627
        self.module_215 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.184
        self.module_217 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.186
        self.module_218 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.187
        self.module_220 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/input.189
        self.module_221 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.190
        self.module_223 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.192
        self.module_224 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.193
        self.module_226 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/23735
        self.module_227 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Cat[cat]/input.195
        self.module_228 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv3]/Conv2d[conv]/input.196
        self.module_230 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv3]/LeakyReLU[act]/input.198
        self.module_231 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv2]/Conv2d[conv]/input.199
        self.module_233 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv2]/LeakyReLU[act]/23792
        self.module_234 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_p1]/input.201
        self.module_235 = py_nndct.nn.Conv2d(in_channels=384, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv1]/Conv2d[conv]/input.202
        self.module_237 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv1]/LeakyReLU[act]/input.206
        self.module_238 = py_nndct.nn.Conv2d(in_channels=384, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv2]/Conv2d[conv]/input.204
        self.module_240 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv2]/LeakyReLU[act]/23849
        self.module_241 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.207
        self.module_243 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.209
        self.module_244 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.210
        self.module_246 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/input.212
        self.module_247 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.213
        self.module_249 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.215
        self.module_250 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.216
        self.module_252 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/23957
        self.module_253 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Cat[cat]/input.218
        self.module_254 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv3]/Conv2d[conv]/input.219
        self.module_256 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv3]/LeakyReLU[act]/input.221
        self.module_257 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv1]/Conv2d[conv]/input.222
        self.module_259 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv1]/LeakyReLU[act]/24014
        self.module_260 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_p0]/input.224
        self.module_261 = py_nndct.nn.Conv2d(in_channels=768, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv1]/Conv2d[conv]/input.225
        self.module_263 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv1]/LeakyReLU[act]/input.229
        self.module_264 = py_nndct.nn.Conv2d(in_channels=768, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv2]/Conv2d[conv]/input.227
        self.module_266 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv2]/LeakyReLU[act]/24071
        self.module_267 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.230
        self.module_269 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/LeakyReLU[act]/input.232
        self.module_270 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.233
        self.module_272 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv2]/LeakyReLU[act]/input.235
        self.module_273 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.236
        self.module_275 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/LeakyReLU[act]/input.238
        self.module_276 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.239
        self.module_278 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv2]/LeakyReLU[act]/24179
        self.module_279 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Cat[cat]/input.241
        self.module_280 = py_nndct.nn.Conv2d(in_channels=768, out_channels=768, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv3]/Conv2d[conv]/input.242
        self.module_282 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv3]/LeakyReLU[act]/input.274
        self.module_283 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[0]/Conv2d[conv]/input.244
        self.module_285 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[0]/LeakyReLU[act]/input.246
        self.module_286 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[0]/Conv2d[conv]/input.247
        self.module_288 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[0]/LeakyReLU[act]/input.249
        self.module_289 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[1]/Conv2d[conv]/input.250
        self.module_291 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[1]/LeakyReLU[act]/input.252
        self.module_292 = py_nndct.nn.Conv2d(in_channels=192, out_channels=45, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[0]/24313
        self.module_293 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[0]/Conv2d[conv]/input.253
        self.module_295 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[0]/LeakyReLU[act]/input.255
        self.module_296 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[1]/Conv2d[conv]/input.256
        self.module_298 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[1]/LeakyReLU[act]/input.258
        self.module_299 = py_nndct.nn.Conv2d(in_channels=192, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[0]/24386
        self.module_300 = py_nndct.nn.Conv2d(in_channels=192, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[0]/24405
        self.module_301 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/Cat[cat_list]/ModuleList[0]/24408
        self.module_302 = py_nndct.nn.dequant_output() #YOLOX::YOLOX/YOLOXHead[head]/DeQuantStub[quant_outs]/ModuleList[0]/24409
        self.module_303 = py_nndct.nn.Conv2d(in_channels=384, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[1]/Conv2d[conv]/input.259
        self.module_305 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[1]/LeakyReLU[act]/input.261
        self.module_306 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[0]/Conv2d[conv]/input.262
        self.module_308 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[0]/LeakyReLU[act]/input.264
        self.module_309 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[1]/Conv2d[conv]/input.265
        self.module_311 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[1]/LeakyReLU[act]/input.267
        self.module_312 = py_nndct.nn.Conv2d(in_channels=192, out_channels=45, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[1]/24510
        self.module_313 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[0]/Conv2d[conv]/input.268
        self.module_315 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[0]/LeakyReLU[act]/input.270
        self.module_316 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[1]/Conv2d[conv]/input.271
        self.module_318 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[1]/LeakyReLU[act]/input.273
        self.module_319 = py_nndct.nn.Conv2d(in_channels=192, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[1]/24583
        self.module_320 = py_nndct.nn.Conv2d(in_channels=192, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[1]/24602
        self.module_321 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/Cat[cat_list]/ModuleList[1]/24605
        self.module_322 = py_nndct.nn.dequant_output() #YOLOX::YOLOX/YOLOXHead[head]/DeQuantStub[quant_outs]/ModuleList[1]/24606
        self.module_323 = py_nndct.nn.Conv2d(in_channels=768, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[2]/Conv2d[conv]/input.275
        self.module_325 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[2]/LeakyReLU[act]/input.277
        self.module_326 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[0]/Conv2d[conv]/input.278
        self.module_328 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[0]/LeakyReLU[act]/input.280
        self.module_329 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[1]/Conv2d[conv]/input.281
        self.module_331 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[1]/LeakyReLU[act]/input.283
        self.module_332 = py_nndct.nn.Conv2d(in_channels=192, out_channels=45, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[2]/24707
        self.module_333 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[0]/Conv2d[conv]/input.284
        self.module_335 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[0]/LeakyReLU[act]/input.286
        self.module_336 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[1]/Conv2d[conv]/input.287
        self.module_338 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[1]/LeakyReLU[act]/input
        self.module_339 = py_nndct.nn.Conv2d(in_channels=192, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[2]/24780
        self.module_340 = py_nndct.nn.Conv2d(in_channels=192, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[2]/24799
        self.module_341 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/Cat[cat_list]/ModuleList[2]/24802
        self.module_342 = py_nndct.nn.dequant_output() #YOLOX::YOLOX/YOLOXHead[head]/DeQuantStub[quant_outs]/ModuleList[2]/24803

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_0 = self.module_7(output_module_0)
        output_module_8 = self.module_8(output_module_0)
        output_module_8 = self.module_10(output_module_8)
        output_module_11 = self.module_11(output_module_0)
        output_module_11 = self.module_13(output_module_11)
        output_module_14 = self.module_14(output_module_8)
        output_module_14 = self.module_16(output_module_14)
        output_module_14 = self.module_17(output_module_14)
        output_module_14 = self.module_19(output_module_14)
        output_module_14 = self.module_20(input=output_module_14, other=output_module_8, alpha=1)
        output_module_21 = self.module_21(output_module_14)
        output_module_21 = self.module_23(output_module_21)
        output_module_21 = self.module_24(output_module_21)
        output_module_21 = self.module_26(output_module_21)
        output_module_21 = self.module_27(input=output_module_21, other=output_module_14, alpha=1)
        output_module_21 = self.module_28(dim=1, tensors=[output_module_21,output_module_11])
        output_module_21 = self.module_29(output_module_21)
        output_module_21 = self.module_31(output_module_21)
        output_module_21 = self.module_32(output_module_21)
        output_module_21 = self.module_34(output_module_21)
        output_module_35 = self.module_35(output_module_21)
        output_module_35 = self.module_37(output_module_35)
        output_module_38 = self.module_38(output_module_21)
        output_module_38 = self.module_40(output_module_38)
        output_module_41 = self.module_41(output_module_35)
        output_module_41 = self.module_43(output_module_41)
        output_module_41 = self.module_44(output_module_41)
        output_module_41 = self.module_46(output_module_41)
        output_module_41 = self.module_47(input=output_module_41, other=output_module_35, alpha=1)
        output_module_48 = self.module_48(output_module_41)
        output_module_48 = self.module_50(output_module_48)
        output_module_48 = self.module_51(output_module_48)
        output_module_48 = self.module_53(output_module_48)
        output_module_48 = self.module_54(input=output_module_48, other=output_module_41, alpha=1)
        output_module_55 = self.module_55(output_module_48)
        output_module_55 = self.module_57(output_module_55)
        output_module_55 = self.module_58(output_module_55)
        output_module_55 = self.module_60(output_module_55)
        output_module_55 = self.module_61(input=output_module_55, other=output_module_48, alpha=1)
        output_module_62 = self.module_62(output_module_55)
        output_module_62 = self.module_64(output_module_62)
        output_module_62 = self.module_65(output_module_62)
        output_module_62 = self.module_67(output_module_62)
        output_module_62 = self.module_68(input=output_module_62, other=output_module_55, alpha=1)
        output_module_69 = self.module_69(output_module_62)
        output_module_69 = self.module_71(output_module_69)
        output_module_69 = self.module_72(output_module_69)
        output_module_69 = self.module_74(output_module_69)
        output_module_69 = self.module_75(input=output_module_69, other=output_module_62, alpha=1)
        output_module_76 = self.module_76(output_module_69)
        output_module_76 = self.module_78(output_module_76)
        output_module_76 = self.module_79(output_module_76)
        output_module_76 = self.module_81(output_module_76)
        output_module_76 = self.module_82(input=output_module_76, other=output_module_69, alpha=1)
        output_module_76 = self.module_83(dim=1, tensors=[output_module_76,output_module_38])
        output_module_76 = self.module_84(output_module_76)
        output_module_76 = self.module_86(output_module_76)
        output_module_87 = self.module_87(output_module_76)
        output_module_87 = self.module_89(output_module_87)
        output_module_90 = self.module_90(output_module_87)
        output_module_90 = self.module_92(output_module_90)
        output_module_93 = self.module_93(output_module_87)
        output_module_93 = self.module_95(output_module_93)
        output_module_96 = self.module_96(output_module_90)
        output_module_96 = self.module_98(output_module_96)
        output_module_96 = self.module_99(output_module_96)
        output_module_96 = self.module_101(output_module_96)
        output_module_96 = self.module_102(input=output_module_96, other=output_module_90, alpha=1)
        output_module_103 = self.module_103(output_module_96)
        output_module_103 = self.module_105(output_module_103)
        output_module_103 = self.module_106(output_module_103)
        output_module_103 = self.module_108(output_module_103)
        output_module_103 = self.module_109(input=output_module_103, other=output_module_96, alpha=1)
        output_module_110 = self.module_110(output_module_103)
        output_module_110 = self.module_112(output_module_110)
        output_module_110 = self.module_113(output_module_110)
        output_module_110 = self.module_115(output_module_110)
        output_module_110 = self.module_116(input=output_module_110, other=output_module_103, alpha=1)
        output_module_117 = self.module_117(output_module_110)
        output_module_117 = self.module_119(output_module_117)
        output_module_117 = self.module_120(output_module_117)
        output_module_117 = self.module_122(output_module_117)
        output_module_117 = self.module_123(input=output_module_117, other=output_module_110, alpha=1)
        output_module_124 = self.module_124(output_module_117)
        output_module_124 = self.module_126(output_module_124)
        output_module_124 = self.module_127(output_module_124)
        output_module_124 = self.module_129(output_module_124)
        output_module_124 = self.module_130(input=output_module_124, other=output_module_117, alpha=1)
        output_module_131 = self.module_131(output_module_124)
        output_module_131 = self.module_133(output_module_131)
        output_module_131 = self.module_134(output_module_131)
        output_module_131 = self.module_136(output_module_131)
        output_module_131 = self.module_137(input=output_module_131, other=output_module_124, alpha=1)
        output_module_131 = self.module_138(dim=1, tensors=[output_module_131,output_module_93])
        output_module_131 = self.module_139(output_module_131)
        output_module_131 = self.module_141(output_module_131)
        output_module_142 = self.module_142(output_module_131)
        output_module_142 = self.module_144(output_module_142)
        output_module_142 = self.module_145(output_module_142)
        output_module_142 = self.module_147(output_module_142)
        output_module_148 = self.module_148(output_module_142)
        output_module_149 = self.module_149(output_module_142)
        output_module_150 = self.module_150(output_module_142)
        output_module_151 = self.module_151(dim=1, tensors=[output_module_142,output_module_148,output_module_149,output_module_150])
        output_module_151 = self.module_152(output_module_151)
        output_module_151 = self.module_154(output_module_151)
        output_module_155 = self.module_155(output_module_151)
        output_module_155 = self.module_157(output_module_155)
        output_module_158 = self.module_158(output_module_151)
        output_module_158 = self.module_160(output_module_158)
        output_module_155 = self.module_161(output_module_155)
        output_module_155 = self.module_163(output_module_155)
        output_module_155 = self.module_164(output_module_155)
        output_module_155 = self.module_166(output_module_155)
        output_module_155 = self.module_167(output_module_155)
        output_module_155 = self.module_169(output_module_155)
        output_module_155 = self.module_170(output_module_155)
        output_module_155 = self.module_172(output_module_155)
        output_module_155 = self.module_173(dim=1, tensors=[output_module_155,output_module_158])
        output_module_155 = self.module_174(output_module_155)
        output_module_155 = self.module_176(output_module_155)
        output_module_155 = self.module_177(output_module_155)
        output_module_155 = self.module_179(output_module_155)
        output_module_180 = self.module_180(input=output_module_155, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_180 = self.module_181(dim=1, tensors=[output_module_180,output_module_131])
        output_module_182 = self.module_182(output_module_180)
        output_module_182 = self.module_184(output_module_182)
        output_module_185 = self.module_185(output_module_180)
        output_module_185 = self.module_187(output_module_185)
        output_module_182 = self.module_188(output_module_182)
        output_module_182 = self.module_190(output_module_182)
        output_module_182 = self.module_191(output_module_182)
        output_module_182 = self.module_193(output_module_182)
        output_module_182 = self.module_194(output_module_182)
        output_module_182 = self.module_196(output_module_182)
        output_module_182 = self.module_197(output_module_182)
        output_module_182 = self.module_199(output_module_182)
        output_module_182 = self.module_200(dim=1, tensors=[output_module_182,output_module_185])
        output_module_182 = self.module_201(output_module_182)
        output_module_182 = self.module_203(output_module_182)
        output_module_182 = self.module_204(output_module_182)
        output_module_182 = self.module_206(output_module_182)
        output_module_207 = self.module_207(input=output_module_182, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_207 = self.module_208(dim=1, tensors=[output_module_207,output_module_76])
        output_module_209 = self.module_209(output_module_207)
        output_module_209 = self.module_211(output_module_209)
        output_module_212 = self.module_212(output_module_207)
        output_module_212 = self.module_214(output_module_212)
        output_module_209 = self.module_215(output_module_209)
        output_module_209 = self.module_217(output_module_209)
        output_module_209 = self.module_218(output_module_209)
        output_module_209 = self.module_220(output_module_209)
        output_module_209 = self.module_221(output_module_209)
        output_module_209 = self.module_223(output_module_209)
        output_module_209 = self.module_224(output_module_209)
        output_module_209 = self.module_226(output_module_209)
        output_module_209 = self.module_227(dim=1, tensors=[output_module_209,output_module_212])
        output_module_209 = self.module_228(output_module_209)
        output_module_209 = self.module_230(output_module_209)
        output_module_231 = self.module_231(output_module_209)
        output_module_231 = self.module_233(output_module_231)
        output_module_231 = self.module_234(dim=1, tensors=[output_module_231,output_module_182])
        output_module_235 = self.module_235(output_module_231)
        output_module_235 = self.module_237(output_module_235)
        output_module_238 = self.module_238(output_module_231)
        output_module_238 = self.module_240(output_module_238)
        output_module_235 = self.module_241(output_module_235)
        output_module_235 = self.module_243(output_module_235)
        output_module_235 = self.module_244(output_module_235)
        output_module_235 = self.module_246(output_module_235)
        output_module_235 = self.module_247(output_module_235)
        output_module_235 = self.module_249(output_module_235)
        output_module_235 = self.module_250(output_module_235)
        output_module_235 = self.module_252(output_module_235)
        output_module_235 = self.module_253(dim=1, tensors=[output_module_235,output_module_238])
        output_module_235 = self.module_254(output_module_235)
        output_module_235 = self.module_256(output_module_235)
        output_module_257 = self.module_257(output_module_235)
        output_module_257 = self.module_259(output_module_257)
        output_module_257 = self.module_260(dim=1, tensors=[output_module_257,output_module_155])
        output_module_261 = self.module_261(output_module_257)
        output_module_261 = self.module_263(output_module_261)
        output_module_264 = self.module_264(output_module_257)
        output_module_264 = self.module_266(output_module_264)
        output_module_261 = self.module_267(output_module_261)
        output_module_261 = self.module_269(output_module_261)
        output_module_261 = self.module_270(output_module_261)
        output_module_261 = self.module_272(output_module_261)
        output_module_261 = self.module_273(output_module_261)
        output_module_261 = self.module_275(output_module_261)
        output_module_261 = self.module_276(output_module_261)
        output_module_261 = self.module_278(output_module_261)
        output_module_261 = self.module_279(dim=1, tensors=[output_module_261,output_module_264])
        output_module_261 = self.module_280(output_module_261)
        output_module_261 = self.module_282(output_module_261)
        output_module_283 = self.module_283(output_module_209)
        output_module_283 = self.module_285(output_module_283)
        output_module_286 = self.module_286(output_module_283)
        output_module_286 = self.module_288(output_module_286)
        output_module_286 = self.module_289(output_module_286)
        output_module_286 = self.module_291(output_module_286)
        output_module_286 = self.module_292(output_module_286)
        output_module_293 = self.module_293(output_module_283)
        output_module_293 = self.module_295(output_module_293)
        output_module_293 = self.module_296(output_module_293)
        output_module_293 = self.module_298(output_module_293)
        output_module_299 = self.module_299(output_module_293)
        output_module_300 = self.module_300(output_module_293)
        output_module_299 = self.module_301(dim=1, tensors=[output_module_299,output_module_300,output_module_286])
        output_module_299 = self.module_302(input=output_module_299)
        output_module_303 = self.module_303(output_module_235)
        output_module_303 = self.module_305(output_module_303)
        output_module_306 = self.module_306(output_module_303)
        output_module_306 = self.module_308(output_module_306)
        output_module_306 = self.module_309(output_module_306)
        output_module_306 = self.module_311(output_module_306)
        output_module_306 = self.module_312(output_module_306)
        output_module_313 = self.module_313(output_module_303)
        output_module_313 = self.module_315(output_module_313)
        output_module_313 = self.module_316(output_module_313)
        output_module_313 = self.module_318(output_module_313)
        output_module_319 = self.module_319(output_module_313)
        output_module_320 = self.module_320(output_module_313)
        output_module_319 = self.module_321(dim=1, tensors=[output_module_319,output_module_320,output_module_306])
        output_module_319 = self.module_322(input=output_module_319)
        output_module_261 = self.module_323(output_module_261)
        output_module_261 = self.module_325(output_module_261)
        output_module_326 = self.module_326(output_module_261)
        output_module_326 = self.module_328(output_module_326)
        output_module_326 = self.module_329(output_module_326)
        output_module_326 = self.module_331(output_module_326)
        output_module_326 = self.module_332(output_module_326)
        output_module_333 = self.module_333(output_module_261)
        output_module_333 = self.module_335(output_module_333)
        output_module_333 = self.module_336(output_module_333)
        output_module_333 = self.module_338(output_module_333)
        output_module_339 = self.module_339(output_module_333)
        output_module_340 = self.module_340(output_module_333)
        output_module_339 = self.module_341(dim=1, tensors=[output_module_339,output_module_340,output_module_326])
        output_module_339 = self.module_342(input=output_module_339)
        return output_module_299,output_module_319,output_module_339
