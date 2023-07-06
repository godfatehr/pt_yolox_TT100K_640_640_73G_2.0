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

# train
export CUDA_VISIBLE_DEVICES=0
GPU_NUM=1
BATCH_SIZE=32
CFG=exps/example/custom/yolox_m_tt100k_qat.py

WEIGHTS=PATH_TO_MODEL

# eval
echo "testing the qat model"
python tools/eval.py -f ${CFG} -c ${WEIGHTS} -b ${BATCH_SIZE} -d 1 --conf 0.001 # --fp16 --fuse

# convert
echo "converted qat model"
CVT_DIR=converted_qat_results
python tools/convert_qat.py -f ${CFG} -c ${WEIGHTS} --cvt_dir ${CVT_DIR}


############################# test the converted results #############################

Q_DIR=${CVT_DIR}
CFG=exps/example/custom/yolox_m_tt100k_quant.py
WEIGHTS=converted_qat_results/converted_qat.pth
echo "test converted qat model"
#
export W_QUANT=1

MODE='test'
python tools/quant.py -f ${CFG} -c ${WEIGHTS} -b ${BATCH_SIZE} -d ${GPU_NUM} --conf 0.001 --quant_mode ${MODE} --quant_dir ${Q_DIR} --nndct_equalization=False --nndct_param_corr=False

echo "dump xmodel for deployment"
MODE='test'
python tools/quant.py -f ${CFG} -c ${WEIGHTS} -b ${BATCH_SIZE} -d ${GPU_NUM} --conf 0.001 --quant_mode ${MODE} --quant_dir ${Q_DIR} --is_dump --nndct_equalization=False --nndct_param_corr=False

