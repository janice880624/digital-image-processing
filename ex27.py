import cv2
img = cv2.imread("photo_video/lena.jpg")
layer = img.copy()
gp = [layer] # Gaussian Pyramid
for i in range(6):
  layer = cv2.pyrDown(layer)
  gp.append(layer) # List
  #cv2.imshow(str(i), layer)
layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer] # Laplacian Pyramid

for i in range(5, 0, -1): # 5, 4, 3, 2, 1
  gaussian_extended = cv2.pyrUp(gp[i])
  laplacian = cv2.subtract(gp[i-1], gaussian_extended)
  lp.append(laplacian)
  cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()