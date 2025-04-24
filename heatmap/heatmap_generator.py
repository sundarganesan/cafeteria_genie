# heatmap/heatmap_generator.py
import cv2
import numpy as np


def generate_heatmap(frame, boxes):
    heatmap = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.float32)

    for (x1, y1, x2, y2) in boxes:
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(heatmap, (cx, cy), radius=25, color=1, thickness=-1)

    heatmap = cv2.GaussianBlur(heatmap, (0, 0), sigmaX=15)
    heatmap = np.clip(heatmap, 0, 1)
    heatmap_color = cv2.applyColorMap((heatmap * 255).astype(np.uint8), cv2.COLORMAP_JET)

    overlay = cv2.addWeighted(frame, 0.6, heatmap_color, 0.4, 0)
    return overlay
