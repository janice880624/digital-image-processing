import numpy as np
import cv2 as cv

cap = cv.VideoCapture('fly.mp4')

ret, frame = cap.read()

c, r, w, h = 490, 230, 260, 110 
track_window = (c, r, w, h)

roi = frame[r:r+h, c:c+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)

l_b = np.array([90, 40, 100])
u_b = np.array([130, 80, 120])
mask = cv.inRange(hsv_roi, l_b, u_b)

roi_hist = cv.calcHist([hsv_roi], [0, 1], mask, [32, 30], [0, 180, 0, 256])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
  ret ,frame = cap.read()

  if ret == True:
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)

    ret, track_window = cv.CamShift(dst, track_window, term_crit)

    pts = cv.boxPoints(ret)
    print(pts)
    pts = np.int0(pts)
    final_image = cv.polylines(frame, [pts], True, 255, 2)

    cv.imshow('dst', dst)
    cv.imshow('final_image', final_image)
    cv.imshow('roi', roi)
    cv.imshow('roi', hsv_roi)

    k = cv.waitKey(60) & 0xff
    if k == 27:
      break
    else:
      cv.imwrite(chr(k) + ".jpg", final_image)

  else:
    break

cv.destroyAllWindows()
cap.release()