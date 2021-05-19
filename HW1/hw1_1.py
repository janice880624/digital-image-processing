import cv2 

img = cv2.imread('../photo_video/messi5.jpg') 
print('shape:{}, size:{}, dtype:{}'.format(img.shape, img.size, img.dtype))

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390] # ROI
img[273:333, 100:160] = ball

cv2.imshow('../photo_video/image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('ball_2.jpg', img)
