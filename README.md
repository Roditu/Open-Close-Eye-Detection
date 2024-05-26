# 👀 Eye Blink Detection (Direct)
Blink detection based on open/close eye image (prototype)
using image templating CNN Keras

## Installation
- Library used:
    - Tensorflow    => Image Tensor processing  
    - Keras         => Build Architecture Deep Learning, Augmentation, LoadData
    - OpenCV        => Image Processing
    - numpy        
    - matplotlib    => Visualizaton

Use the package manage [pip](https://pip.pypa.io/en/stable/installation/).
```bash
pip install tensorflow
pip install tf_keras
pip install opencv-python
pip install numpy
pip install matplotlib
```

## Code Structure
- Tensorflow (300MB) -> tf lite (130MB)
- Preprocesssing:
    - image size: 128,128
    - color mode: grayscale
    - batch size: 16

- Augmentation
    - Contrast
    - rotate
    - zoom
    - translation

- Using CNN layer:
    - Featured Extraction:
        - Convolutional 2D
        - Max Pooling Layer
        - Convolutional 2D
        - Max Pooling Layer
    
    - Classification:
        - Flatten Layer
        - Dense Layer
        - Dense Layer (Output)

    - Optimizer : Adam (lr: 0.001)
    - loss      : BinaryCrossentropy
    - metrics   : Accuracy


- Result :
    - Tensorflow (h5):
        PrecisionL0.7190265655517578, 
        Recall:0.9789156913757324, 
        Bi Accuracy:0.7859424948692322

- Inference
    Expected input image shape numpy:  (1, 128, 128, 1) / tensor for tflite

Tensorflow lite works in differnt ways, so it requires its own special interpreter

dataset from:
https://universe.roboflow.com/phoenix-bpovw/drowsiness-detection-n9uj5
https://universe.roboflow.com/university-of-jeddah-xnqit/-new-drwosy-driver-detection

I merge two of that dataset to become one and split it into 3 folder:
- train
- test
- valid

Each folder has 2 class:
- Opened Eye
- Closed Eye