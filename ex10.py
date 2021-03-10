import cv2 ex10.py

img = cv2.imread('photo_video/messi5.jpg') # 548x342
print(img.shape) # (row, column, channel)
print(img.size) # total no. of pixels
print(img.dtype) # image dadatype

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

cv2.imshow('photo_video/image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()