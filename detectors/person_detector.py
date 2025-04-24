from ultralytics import YOLO

# Load a pretrained model (once globally)
model = YOLO("yolov5s.pt")  # You can try 'yolov8n.pt' too if you want to switch later

def detect_people(frame):
    results = model(frame, verbose=False)[0]
    people_boxes = []
    for r in results.boxes:
        cls_id = int(r.cls)
        if cls_id == 0:  # class 0 = person
            x1, y1, x2, y2 = map(int, r.xyxy[0])
            people_boxes.append((x1, y1, x2, y2))
    return people_boxes
