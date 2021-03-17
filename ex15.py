import cv2 as cv

def nothing(x):
    print(x)

cv.namedWindow('photo_video/image')

cv.createTrackbar('CP', 'photo_video/image', 0, 255, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'photo_video/image', 0, 1, nothing)

while(1):
    img = cv.imread('photo_video/lena.jpg')
    pos = cv.getTrackbarPos('CP', 'photo_video/image')

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv.getTrackbarPos(switch, 'photo_video/image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('photo_video/image', img)
cv.destroyAllWindows()