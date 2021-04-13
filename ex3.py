import cv2
#開啟攝像頭 => 第一隻
#cv2.CAP_DSHOW => microsoft 特有的用於防止釋放 camera 時的 warn
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #0為電腦內建攝像頭
cap = cv2.VideoCapture(0) 
# cap = cv2.VideoCapture('photo_video/vtest.avi')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 高度
fps = int(cap.get(cv2.CAP_PROP_FPS)) # 速度

# 保存
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', codec, 20.0, (width, height))

print(cap.isOpened()) # True

while (cap.isOpened()):

    # 從攝影機擷取一張影像 ret => 是否成功  frame => 攝影機的單張畫面
    ret, frame = cap.read()

    if ret == True:

        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print('width:{} height:{}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        out.write(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 釋放攝影機
cap.release()
out.release()
cv2.destroyAllWindows()