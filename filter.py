import cv2
import numpy as np
# img = cv2.imread("photo_video/messi5.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("photo_video/sudoku.png", cv2.IMREAD_GRAYSCALE)

# lap
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# dst
kernel = np.ones((3,3), np.float32)
kernel[1][1]=-8
dst = cv2.filter2D(img,-1, kernel)

# log
kernel1 = np.array([[0, 1, 1, 2, 2, 2, 1, 1, 0],[1, 2, 4, 5, 5, 5, 4, 2, 1],
    [1, 4, 5, 3, 0, 3, 5, 4, 1],[2, 5, 3, -12, -24, -12, 3, 5, 2],
    [2, 5, 0, -24, -40, -24, 0, 5, 2],[2, 5, 3, -12, -24, -12, 3, 5, 2],
    [1, 4, 5, 3, 0, 3, 5, 4, 1],[1, 2, 4, 5, 5, 5, 4, 2, 1],
    [0, 1, 1, 2, 2, 2, 1, 1, 0]], dtype = np.float32)

log = cv2.filter2D(img,-1, kernel1)

cv2.imshow('img', img)
cv2.imshow('lap', lap)
cv2.imshow('dst', dst)
cv2.imshow('log', log)

cv2.waitKey(0)
cv2.destroyAllWindows()