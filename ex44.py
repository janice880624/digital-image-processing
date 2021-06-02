import cv2 as cv

cap = cv.VideoCapture('photo_video/vtest.avi')

fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
  ret, frame = cap.read()
  if frame is None:
    break
  fgmask = fgbg.apply(frame)

  cv.imshow('Frame', frame)
  cv.imshow('FG MASK Frame', fgmask)

  keyboard = cv.waitKey(30)
  if keyboard == 'q' or keyboard == 27:
    print(fgbg.getHistory())
    break
cap.release()
cv.destroyAllWindows()