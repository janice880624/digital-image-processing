import cv2
import numpy as np

def save_image(image,addr,num):
  address = addr + str(num)+ '.jpg'
  cv2.imwrite(address,image)

videoCapture = cv2.VideoCapture("slow_traffic_small.mp4")

success, frame = videoCapture.read()

i = 0
timeF = 50
j=0

while success :
  i = i + 1
  if (i % timeF == 0):
    j = j + 1
    save_image(frame,'./output/image',j)
    print('save image:',i)
  success, frame = videoCapture.read()

