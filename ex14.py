import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
    #pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('photo_video/image')

cv.createTrackbar('B', 'photo_video/image', 0, 255, nothing)
cv.createTrackbar('G', 'photo_video/image', 0, 255, nothing)
cv.createTrackbar('R', 'photo_video/image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'photo_video/image', 0, 1, nothing)

while(1):
    cv.imshow('photo_video/image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc key
        break
    b = cv.getTrackbarPos('B', 'photo_video/image')
    g = cv.getTrackbarPos('G', 'photo_video/image')
    r = cv.getTrackbarPos('R', 'photo_video/image')
    s = cv.getTrackbarPos(switch, 'photo_video/image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()