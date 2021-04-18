# -*- coding: utf-8 -*-
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('photo_video/noisy2.png',0) # grayscale

# 第一種情況，採用值為127的全域性閾值
# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Otsu的二值化
# 第二種情況，直接採用Otsu閾值法
# 在全域性閾值化中，我們使用任意選擇的值作為閾值。相反，Otsu的方法避免了必須選擇一個值並自動確定它的情況。
ret2,th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# 第三種情況，使用5×5高斯核對影象進行濾波以去除噪聲，然後應用Otsu閾值處理
blur = cv.GaussianBlur(img,(5,5),0) # see 18 blurring image
ret3,th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1, 
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()