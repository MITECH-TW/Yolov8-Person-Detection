from ultralytics import YOLO
import cv2
from imutils.video import VideoStream
import time

output_shape = (640, 480)  
video_name = 'output.mp4'

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS) 
print("FPS of the webcam is: ", fps)

vs = VideoStream(src=0).start()
time.sleep(3)

model = YOLO('./model/yolov8s-seg-person.pt')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_name, fourcc, fps, output_shape)

prev_time = time.time()

while True:
    frame = vs.read()
    out.write(frame)
    frame_resize = cv2.resize(frame, output_shape) 
    results = model(frame_resize, classes=[0], conf=0.8)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Inference", annotated_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:
        break


out.release()
vs.stop()
cv2.destroyAllWindows()