import numpy as np
import cv2

img = cv2.imread('photo_video/shape.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow("img", img)

for contour in contours:
  approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
  cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
  # x = approx[0][0][0]
  # y = approx[0][0][1]- 15

  x, y = approx[0][0][:]
  y = y-15

  print(x, y)
  if len(approx) == 3:
    cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
  elif len(approx) == 4:
    x1, y1, w, h = cv2.boundingRect(approx)
    aspectRatio = float(w)/h
    print(aspectRatio)
    if aspectRatio >= 0.95 and aspectRatio <= 1.2:
      cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
      cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
  elif len(approx) == 5:
    cv2.putText(img, "Pentagon", (x, y-70), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
  elif len(approx) == 10:
    cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
  else:
    cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.imshow("shape", img)
cv2.waitKey(0)
cv2.destroyAllWindows()