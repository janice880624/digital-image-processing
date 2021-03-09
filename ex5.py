import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480
print('width:{} height:{}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cap.set(3, 1280) # highest resolution
cap.set(4, 720) # highest resolution
print(cap.get(3))
print(cap.get(4))

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