import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('photo_video/gradient.png', 0)

ret, thresh1 = cv.threshold(img, 127, 255, cd.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cd.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cd.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cd.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, THRESH_TOZERO_INV)

titles = ['Orignal Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

images = [img, thresh1], thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(image[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

