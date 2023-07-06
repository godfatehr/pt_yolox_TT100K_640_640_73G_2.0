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

#!/bin/bash

# Download the tt100k data in datasets dir
cd datasets
unzip data.zip
cd data
#
echo "Start the converted dataset"
python ../convert.py --gt_json_filename annotations.json

rm -rf train/*.txt
rm -rf test/*.txt
mkdir tt100k
mv train tt100k/train2017
mv test tt100k/val2017
mv annotations tt100k/
