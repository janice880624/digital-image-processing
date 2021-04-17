import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #0為電腦內建攝像頭
cap = cv2.VideoCapture(0)

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480
print('width:{} height:{}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# VGA = 640 x 480
# HD = 1280 x 720
# FHD = 1920 x 1080
# 4K = 3840 x 2160
cap.set(3, 1280) # 3 -> 寬
cap.set(4, 720) # 4 -> 高
# print(cap.get(3))
# print(cap.get(4))
print('width:{} height:{}'.format(cap.get(3), cap.get(4)))

print(cap.isOpened()) # True

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray video', frame) # show gray video

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()