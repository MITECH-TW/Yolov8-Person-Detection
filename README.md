# Fine-tuning YOLOv8s-seg for Person Detection

This repository contains the necessary files and instructions to fine-tune the YOLOv8s-seg model for the specific task of detecting "people" in images or videos, simplifying the original COCO dataset's 80 categories to just "person". Any objects contained within the outline of a person are considered part of the person for detection purposes.

## Environment Setup

1. Install Pytorch
   ```
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```
2. Install Python requirements:
   ```
   pip install -r requirements.txt
   ```

## Training Instructions

### Step 1: Fine-Tune YOLOv8s-seg

Start by fine-tuning the YOLOv8s-seg model with the command below:

```bash
python trainYOLOV8.py
```

This process automatically downloads the COCO dataset. Once the download is complete, training begins. You may observe some training errors due to modifications in the `coco.yaml` file. Ignore these errors and proceed to Step 2.

### Step 2: Execute labelFilter
Run:
```
python labelFilter.py
```
After execution, two new folders `train2017_person` and `val2017_person` will be created under `./datasets/coco/labels/`, containing labels of images with persons. Additionally, two new files, `train2017.txt` and `val2017.txt`, will be generated in `./datasets/coco/labels/` listing the images that include persons. Now, add all paths from `train_bg.txt` and `val_bg.txt` back into the new `train2017.txt` and `val2017.txt` to ensure some background images are included in the training.

### Step 3: Replace train2017.txt and val2017.txt
Replace the `train2017.txt` and `val2017.txt` files in `./datasets/coco/` with the new ones from `./datasets/coco/labels/`.

### Step 4: Rename train2017_person and val2017_person
Delete the old `train2017` and `val2017` folders in `./datasets/coco/labels`. Rename `train2017_person` and `val2017_person` to `train2017` and `val2017`, respectively.

### Step 5: Re-run trainYOLOV8.py

Run the training script again to fine-tune the YOLOv8 model to detect only persons:
```
python trainYOLOV8.py
```

## Quickstart

Download [`yolov8s-seg-person.pt`](https://drive.google.com/file/d/1kf1xVbOEisq9RP3Fes-KijL5Vs_bbvmh/view?usp=sharing), our fine-tune model, and place it in the `model` folder. To see the model in action, run:
```
python infer-webcam.py
```
and you will be able to see the model detecting persons in real-time.
