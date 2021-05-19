import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('photo_video/lena.jpg')
b, g, r = cv.split(img)
cv.imshow("img", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

plt.hist(b.ravel(), 256, [0, 256], color="b")
plt.hist(g.ravel(), 256, [0, 256], color="g")
plt.hist(r.ravel(), 256, [0, 256], color="r")

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()