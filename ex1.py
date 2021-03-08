import cv2

# 灰階模式(單通道)
img = cv2.imread('photo_video/lena.jpg', 0)
print(img.shape)

# 彩色(三通道)
img2 = cv2.imread('photo_video/lena.jpg', 1)
print(img2.shape)

# 彩色(透過解碼)
img3 = cv2.imread('photo_video/lena.jpg', -1)
print(img3.shape)