# utils/video_utils.py
import cv2
from detectors.person_detector import detect_people
from heatmap.heatmap_generator import generate_heatmap
# from .video_utils import get_video_frames

def get_video_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()


def process_video_feed(source_id, video_path):
    print(f"[{source_id}] Starting feed: {video_path}")
    for idx, frame in enumerate(get_video_frames(video_path)):
        boxes = detect_people(frame)
        heatmap_frame = generate_heatmap(frame, boxes)

        # Draw person count and bounding boxes
        count = len(boxes)
        cv2.putText(heatmap_frame, f"People: {count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        for (x1, y1, x2, y2) in boxes:
            cv2.rectangle(heatmap_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # FPS (optional, simplified)
        cv2.putText(heatmap_frame, f"Feed: {source_id}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 255, 200), 2)

        cv2.imshow(f"{source_id} - Cafeteria Genie", heatmap_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()