# detector.py
from ultralytics import YOLO

# Load YOLO model globally so it's not reloaded on every frame
model = YOLO("yolov8n.pt")  # You can replace this with your trained model path

def detect_objects(image):
    results = model(image)[0]
    annotated_image = results.plot()
    detected_classes = [model.names[int(cls)] for cls in results.boxes.cls]
    return annotated_image, list(set(detected_classes))
