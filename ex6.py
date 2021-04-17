# 顯示時間在畫面
import cv2
import datetime

cap = cv2.VideoCapture(0) 
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480
print('width:{} height:{}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(cap.isOpened()) # True

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(datetime.datetime.now())

        # cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('date time', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()