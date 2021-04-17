import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255, 0, 0), 5)
        cv2.imshow('photo_video/image', img)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('photo_video/image', img)
points = []

cv2.setMouseCallback('photo_video/image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows