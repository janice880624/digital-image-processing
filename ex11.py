import cv2 

img = cv2.imread('photo_vodeo/messi5.jpg') # 548x342
print(img.shape) # (row, column, channel)
print(img.size) # total no. of pixels
print(img.dtype) # image dadatype

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390] # ROI
img[273:333, 100:160] =ball

cv2.imshow('photo_vodeo/image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()