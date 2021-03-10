import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('photo_vodeo/image', img)
        mycolorImage = np.zeros((512, 512, 3), np.uint8) # black image
        mycolorImage[:] = [blue, gre    en, red]
        cv2.imshow('photo_vodeo/color',mycolorImage)

img = cv2.imread('photo_vodeo/lena.jpg')
cv2.imshow('photo_vodeo/image', img)
cv2.setMouseCallback('photo_vodeo/image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()