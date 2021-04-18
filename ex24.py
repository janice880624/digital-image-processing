import cv2
import numpy as np
from matplotlib import pyplot as plt

# 灰階
img = cv2.imread("photo_video/lena.jpg", cv2.IMREAD_GRAYSCALE)

# Laplacian算子 
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# 利用Sobel算子進行圖像梯度計算
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

# edges = cv2.Canny(gray, low_threshold, high_threshold)
canny = cv2.Canny(img,100,200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.imshow('image', img)
cv2.imshow('Laplacian', lap )
cv2.imshow('sobelX', sobelX)
cv2.imshow('sobelY', sobelY)
cv2.imshow('sobelCombined', sobelCombined)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()