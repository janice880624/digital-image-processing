# 影像模糊化
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 影像轉換
img = cv2.imread('photo_video/water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)

# 取平均
kernel = np.ones((5, 5), np.float32)/25

# 2D Convolution ( Image Filtering )
# dst = cv.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
# ddepth -> 目標圖像的所需深度 (-1, 結果（目標）圖像將具有與輸入（源）圖像相同的深度)
# kernal -> 卷積核
dst = cv2.filter2D(img, -1, kernel)

# 平均濾波 Averaging
blur = cv2.blur(img, (5, 5))

# 高斯濾波 Gaussian Filtering
# dst = cv2.GaussianBlur(src，ksize，sigmaX [，DST [，sigmaY [，borderType ] ] ] ）
# σ（空間的標準差）:0 程式自動計算
gblur = cv2.GaussianBlur(img, (5, 5), 0)

# 中值濾波 Median Filtering
median = cv2.medianBlur(img, 5)

# 雙邊濾波 Bilateral Filtering
# dst = cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# color σ即顏色空間的標準差，愈大代表在計算時需要考慮更多的顏色。
# space σ即坐標空間的標準差，這個參數與Guassian filter使用的相同，數值越大，代表越遠的像素有較大的權值。
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()