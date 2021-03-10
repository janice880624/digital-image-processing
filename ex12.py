import cv2

img = cv2.imread('photo_video/messi5.jpg') # 548x342
img2 = cv2.imread('photo_video/opencv-logo.png') # 600x794

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, 0.5, img2, 0.1, 0)

cv2.imshow('photo_video/image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()