# HW4
## 方法一 CamShift

https://youtu.be/wJXv6AJMsnM

### main code
https://github.com/janice880624/digital-image-processing/blob/main/final/final.py

### step.1 擷取照片
https://github.com/janice880624/digital-image-processing/blob/main/final/get_photo.py

### step.2 找 roi 位置
https://github.com/janice880624/digital-image-processing/blob/main/final/point.py

讀取 step.1 所擷取的照片來得到戰鬥機的確切位置

### step.3 得到 hsv 的值
https://github.com/janice880624/digital-image-processing/blob/main/final/hsv.py

### step.4 測試
https://github.com/janice880624/digital-image-processing/blob/main/final/range.py

---

## 方法二

https://youtu.be/SPKDw3yxa3U

### main code
https://github.com/janice880624/digital-image-processing/blob/main/final/MOG2.py

step.1 cv2.getStructureElement 構造形態學的卷積) 

step.2 cv2.createBackgroundSubtractorMOG2(構造高斯混合模型) 

step.3 cv2.morpholyEx(對圖像進行形態學的變化)

step.4 找出適當的 length 設定範圍

---

## 結論
方法一與二各有優缺點，方法一事先將影片處理後，調整域質，找出我們要的；方法二是透過長度來找出我們需要的