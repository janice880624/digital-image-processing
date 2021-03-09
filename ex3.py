import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture('vtest.avi')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', codec, 20.0, (width, height))

print(cap.isOpened()) # True

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print('width:{} height:{}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        out.write(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
        cv2.imshow('gray video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()