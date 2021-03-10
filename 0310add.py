import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
        cv2.imshow('photo_video/image', img)
        

    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
        cv2.imshow('photo_vodeo/image', img)

img = cv2.imread('photo_video/lena.jpg')
cv2.imshow('photo_video/image', img)

cv2.setMouseCallback('photo_video/image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows