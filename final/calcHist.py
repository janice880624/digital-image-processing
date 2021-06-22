import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./output/image1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = np.zeros(gray.shape, np.uint8)
mask[347:434, 370:564]  = 255

masked_gray = cv2.bitwise_and(gray, gray, mask = mask)

hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])

hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(gray, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_gray, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()