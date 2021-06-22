import cv2 as cv
from matplotlib import pyplot as plt

winName = 'getTrackbarPos'
# 新建窗口
cv.namedWindow(winName, cv.WINDOW_NORMAL)

def nothing(): pass

cv.createTrackbar('hue', winName, 60, 180, nothing)
cv.createTrackbar('sat', winName, 60, 256, nothing)

def back_projection_demo(): 
  test = cv.imread("roi.jpg") 
  roi_hsv = cv.cvtColor(test, cv.COLOR_BGR2HSV) 
  target = cv.imread("./output/image5.jpg") 
  target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV) 
  cv.imshow("sample", test) 
  cv.imshow("target", target) 
  while(1): 
    # 从滑动条读取数据 
    hue = cv.getTrackbarPos('hue', winName) 
    sat = cv.getTrackbarPos('sat', winName) 
    print(hue, sat)
    # 计算直方图 
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [ hue, sat], [0, 180, 0, 256]) 
    # 获取直方图的反向投影 
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1) 
    cv.imshow(winName, dst) 
    if cv.waitKey(1) == ord('q'): 
      break


back_projection_demo()
cv.destroyAllWindows()

# image1 [2, 161]