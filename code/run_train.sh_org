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
export CUDA_VISIBLE_DEVICES=0,1,2,3
GPU_NUM=4
BATCH_SIZE=32
CFG=exps/example/custom/yolox_m_tt100k_float.py
python tools/train.py -f ${CFG} -d ${GPU_NUM} -b 64 --fp16

WEIGHTS=../float/best_ckpt.pth

# eval
python tools/eval.py -f ${CFG} -c ${WEIGHTS} -b ${BATCH_SIZE} -d 1 --conf 0.001 # --fp16 --fuse

