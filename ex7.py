import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ',' str(y)