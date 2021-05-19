import cv2

img = cv2.imread("photo_video/messi5.jpg")

x = 335
y = 280
w = 60
h = 60

crop_img = img[y:y+h, x:x+w]

cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
