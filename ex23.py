import cv2
import numpy as np
from matplotlib import pyplot as plt

# 灰階
img = cv2.imread("photo_video/messi5.jpg", cv2.IMREAD_GRAYSCALE)

# Laplacian算子 -> 圖像中的邊緣區域，像素值會發生“跳躍”，對這些像素求導
# 先用 Sobel 算子計算二階x和y導數，再求和
# dst = cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
# cv2.CV_64F 表示 64 位浮點數即 64float
# ksize是算子的大小，必須為1、3、5、7。默認為1。
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])
# 利用Sobel算子進行圖像梯度計算
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# -------------------------------- #

# dst=cv2.Scharr(src,ddpetph,dx,dy)
ScharrX = cv2.Scharr(img, cv2.CV_64F, 1, 0)
ScharrY = cv2.Scharr(img, cv2.CV_64F, 0, 1)

ScharrX = np.uint8(np.absolute(ScharrX))
ScharrY = np.uint8(np.absolute(ScharrY))

# -------------------------------- #
# sobel 與 scharr 大小一樣，因此計算量一樣
# scharr 算子可以計算出更小的梯度變化，也因臨近像素的權重更大，故精準度更高
# -------------------------------- #

sobelCombined_1 = cv2.bitwise_or(sobelX, sobelY)
sobelCombined_2 = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

Scharr_1 = cv2.bitwise_or(ScharrX, ScharrY)
Scharr_2 = cv2.addWeighted(ScharrX, 0.5, ScharrY, 0.5, 0)

titles = ['sobel_bitwise_or', 'sobel_addWeighted', 'Scharr_bitwise_or', 'Scharr_addWeighted']
images = [sobelCombined_1, sobelCombined_2, Scharr_1, Scharr_2]
for i in range(4):
   plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()

#titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
#images = [img, lap, sobelX, sobelY, sobelCombined]
#for i in range(5):
#    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

#cv2.imshow('image', img)
#cv2.imshow('Laplacian', lap )
#cv2.imshow('sobelX', sobelX)
#cv2.imshow('sobelY', sobelY)
cv2.imshow('sobel_bitwise_or', sobelCombined_1)
cv2.imshow('sobel_addWeighted', sobelCombined_2)
cv2.imshow('Scharr_bitwise_or', Scharr_1)
cv2.imshow('Scharr_addWeighted', Scharr_2)

cv2.waitKey(0)
cv2.destroyAllWindows()