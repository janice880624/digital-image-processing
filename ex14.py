import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
    #pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('photo_vodeo/image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc key
        break
    b = cv.getTrackbarPos('B', 'photo_vodeo/image')
    g = cv.getTrackbarPos('G', 'photo_vodeo/image')
    r = cv.getTrackbarPos('R', 'photo_vodeo/image')
    s = cv.getTrackbarPos(switch, 'photo_vodeo/image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()