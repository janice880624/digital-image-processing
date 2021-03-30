import cv2

# 灰階模式(單通道)
img = cv2.imread('photo_video/lena.jpg', 0)
print(img.shape)
# (512, 512)

# 彩色(三通道) -> 預設
img2 = cv2.imread('photo_video/lena.jpg', 1)
print(img2.shape)
# (512, 512, 3)

# 彩色(透過解碼)
img3 = cv2.imread('photo_video/lena.jpg', -1)
print(img3.shape)
# (512, 512, 3)

# 建立視窗
cv2.imshow('photo_video/lena image', img)

# 0 -> 持續等待至使用者按下任意按鍵時結束
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()

cv2.imwrite('photo_video/lena_copy.png', img)
