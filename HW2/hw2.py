import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# 讀取照片
img = cv2.imread("hw2.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
faces = face_cascade.detectMultiScale(gray_img, 1.1, 1)

for (x, y , w ,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
    faceROI = gray_img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(faceROI, 1.2, 1)
    for (x2, y2 ,w2, h2) in eyes:
        eye_center = (x + x2 + w2//2, y + y2 + h2//2)
        radius = int(round((w2 + h2)*0.25))
        frame = cv2.circle(img, eye_center, radius, (0, 0, 255), 3)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('hw2_ans.jpg', img)