import cv2
import numpy as np

img = cv2.imread("photo_video/sudoku.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow("edges", edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 160)

for line in lines:
  rho, theta = line[0]
  c = np.cos(theta)
  s = np.sin(theta)
  x0 = c * rho
  y0 = s * rho
  x1 = int(x0 + 1000*(-s))
  y1 = int(y0 + 1000*(c))
  x2 = int(x0 - 1000*(-s))
  y2 = int(y0 - 1000*(c))
  cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Hough Lines', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()