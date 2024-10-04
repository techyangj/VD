# Pay Attention

This is the implementation of this paper: Verifying in the Dark: Verifiable Machine Unlearning by Using Invisible Backdoor Triggers. (IEEE TRANSACTIONS ON INFORMATION FORENSICS AND SECURITY, VOL. 19, 2024) 

**Problems with the original code: only part of the code is provided, and it cannot be run on Windows systems. There is also a lack of data set integration and parameter settings.**）

## Installation 

Requires Pytorch and CUDA. Our implementation was tested on Ubuntu 20.04 and Windows.

### Model

Knowledge Distillation + Resnet34 + Incremental Learning

### How to Run 

Downloading 

```
cd add_code
python crifa_download.py / mnist_download.py
```

Processing the dataset

```p
python class_name_convert.py  
python size_convert.py 
```

allocate dataset to Clients

```
python allocate.py
```

Poisoning data(LSB), opening a backdoor in data

```
python backdoor.py
```

### Train

```
python train.py
```



