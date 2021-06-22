import cv2
import numpy as np

def nothing(x):
    pass

while True:
  frame = cv2.imread('./output/image1.jpg')

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#   l_b = np.array([100, 60, 80])
#   u_b = np.array([120, 105, 120])

  l_b = np.array([105, 40, 130])
  u_b = np.array([110, 60, 190])

  # mask = cv2.inRange(hsv, lower_red, upper_red)
  # lower_red 指的是圖像中低於這個 lower_red 的值，圖像值變為 0
  # upper_red 指的是圖像中高於這個 upper_red 的值，圖像值變為 0
  mask = cv2.inRange(hsv, l_b, u_b)

  # 將遮罩印在原來的圖片上，有點像挖空的感覺
  res = cv2.bitwise_and(frame, frame, mask=mask)

  cv2.imshow("frame", frame)
  cv2.imshow("mask", mask)
  cv2.imshow("res", res)

  key = cv2.waitKey(1)
  if key == 27:
      break

cv2.destroyAllWindows()