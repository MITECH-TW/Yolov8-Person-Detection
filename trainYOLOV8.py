from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s-seg.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='./coco.yaml', epochs=50, imgsz=640,batch=16,optimizer='Adam',lr0=0.00001,lrf=0.0000001)