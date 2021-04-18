import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('photo_video/gradient.png', 0)

# ret, out = cv2.threshold(img, thresh, max, method)
# thresh -> 最小門檻值 max -> 最大門檻值
# 只能處理灰階影像（二值化）

# Threshold Binary：即二值化，將大於閾值的灰度值設為最大灰度值，小於閾值的值設為0。
# Threshold Binary, Inverted：將大於閾值的灰度值設為0，其他值設為最大灰度值。
# Truncate：將大於閾值的灰度值設為閾值，小於閾值的值保持不變。
# Threshold to Zero：將小於閾值的灰度值設為0，大於閾值的值保持不變。
# Threshold to Zero, Inverted：將大於閾值的灰度值設為0，小於閾值的值保持不變。

ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Orignal Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

