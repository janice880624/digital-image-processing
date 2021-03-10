import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ',' + str(y)
        cv2.putText(img, text, (x, y), font, 0.5, (255 ,255 ,0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, text, (x, y), font, 0.5, (0 ,255 ,255), 2, cv2.LINE_AA)
        cv2.imshow('image', img)

img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows