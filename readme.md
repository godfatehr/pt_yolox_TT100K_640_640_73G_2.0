# TSD_YoloX for traffic sign detection
### Contents
1. [Installation](#installation)
2. [Preparation](#preparation)
3. [Eval/Test](#eval/test)
4. [Performance](#performance)
5. [Model_info](#model_info)

### Installation
1. Environment requirement
    - pytorch, opencv, more details seen in requirements.txt
    - vai_q_pytorch(Optional, required by quantization)
    - XIR Python frontend (Optional, required by quantization)

2. Installation with Docker

   - Please refer to [vitis-ai](https://github.com/Xilinx/Vitis-AI/tree/master/) for how to obtain the docker image.

   - Activate pytorch virtual envrionment in docker:
   ```shell
   conda activate vitis-ai-pytorch
   ```
   - Install all the python dependencies using pip:
   ```shell
   pip install --user -r requirements.txt
   ```
   - Compile the yolox using pip:
   ```shell
   pip install --user -v -e .
   ```

### Preparation

1. Dataset description
   - download TT100k dataset in code/datasets/.

2. Dataset diretory structure
   ```
   + data/
     + annotationsi.json
     + lmdb
     + marks
     + other
     + train
     + test
   ```
3. Prepare dataset required by model.
   ```
   cd code/datasets/ 
   bash convert_label.sh
   ```

### Eval/Test

1. Training 

    ```shell
    cd code/

    bash run_train.sh 
    ```
2. Demo
    ```shell
    cd code/

    bash run_demo.sh
    ```
3. Quantization
    ```shell
    cd code/

    bash quant_PTQ.sh
    ```
4. QAT Training(quantizing model directly would lead large accuracy drop, so we provide quantization training scripts to improve quantization accuracy.)
   ```shell
   cd code/

   bash quant_QAT.sh 
   ```    
6. QAT Testing and Dump xmodel
   ```shell
   cd code/

   bash qat_convert.sh 
   ```    

### Performance
Noteperformance is evaluated on TT100k val.
- Float model

| model | input size | FLOPs | AP|
|-------|------------|--------------|-----------|
| YOLOx-m-modified| 640x640 | 72.96G | 62.3 |

- QAT model

| model | input size | FLOPs | INT8 AP|
|-------|------------|--------------|-----------|
| YOLOx-m-modified| 640x640 | 72.96G | 62.1 |

### Model_info

1. Data preprocess
  ```
  data channel order: RGB(0~255)                  
  input size: h * w = 640 * 640
  mean = (0.0, 0.0, 0.0)
  std = (1.0, 1.0, 1.0)
  input = (input * normalize  - mean) / std
  ```
