import numpy as np
import cv2 as cv

lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

cap = cv.VideoCapture('photo_video/slow_traffic_small.mp4')

while(1):
    ret, frame = cap.read()

    if ret == True:

      hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
      mask = cv.inRange(hsv, lower_green, upper_green)
      res = cv.bitwise_and(frame, frame, mask=mask)

      cv.imshow('frame', frame)
      cv.imshow('mask', mask)
      cv.imshow('res', res)
      
      k = cv.waitKey(30) & 0xff
      if k == 27:
          break
    else:
        break