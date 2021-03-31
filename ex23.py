import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("photo_video/messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

ScharrX = cv2.Scharr(img, cv2.CV_64F, 1, 0)
ScharrY = cv2.Scharr(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined_1 = cv2.bitwise_or(sobelX, sobelY)
sobelCombined_2 = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

Scharr_1 = cv2.bitwise_or(ScharrX, ScharrY)
Scharr_2 = cv2.addWeighted(ScharrX, 0.5, ScharrY, 0.5, 0)

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