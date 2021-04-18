import cv2
from matplotlib import pyplot as plt

# 彩色(透過解碼)
img1 = cv2.imread('photo_video/lena.jpg', -1)
cv2.imshow('image', img1)

img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img2)

plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2: BGR
# matplotlib: RGB