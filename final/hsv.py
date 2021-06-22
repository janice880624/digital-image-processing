import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('test.jpg')
# HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def getpos(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(image[y,x])

# cv2.imshow("imageHSV", HSV)
cv2.imshow('image', image)
cv2.setMouseCallback("image", getpos)
cv2.waitKey(0)


# [108  95  86]
# [108  95  86]
# [111  82  84]
# [108  93  88]
# [111  82  84]
# [109  79  94]
# [111  81  85]
# [110  85  78]

