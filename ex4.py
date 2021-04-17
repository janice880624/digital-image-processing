import numpy as np
import cv2
img = cv2.imread('photo_video/lena.jpg',1) # color (default)
# img = np.zeros([512, 512, 3], np.uint8) # black image

# cv2.line(影像, 開始座標, 結束座標, 顏色, 線條寬度)
img = cv2.line(img, (0, 0), (255, 255), (255, 153, 187), 10) # color=(b,g,r)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

# cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

# cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1) # fill in

# cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('geomatric image',img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()