import cv2
import numpy as np

img = cv2.imread("photo_video/messi5.jpg") # shape (342, 548, 3)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # shape (342, 548)
template = cv2.imread("photo_video/cut.jpg", 0) # shape (52, 40)
w, h = template.shape[::-1] # w=40, h=52

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED )
print(res)
threshold = 0.97
loc = np.where(res >= threshold)
print(loc) #(array([85], dtype=int64), array([220], dtype=int64))

for pt in zip(*loc[::-1]):
  cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()