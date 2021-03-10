import cv2

img = cv2.imread('photo_vodeo/messi5.jpg') # 548x342
img2 = cv2.imread('photo_vodeo/opencv-logo.png') # 600x794

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, 0.2, img2, 0.8, 0)

cv2.imshow('photo_vodeo/image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()