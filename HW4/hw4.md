# HW4

### main code
結合了 tesseract 與 muggle 方法
https://github.com/janice880624/digital-image-processing/blob/main/HW4/hw4.py

### tesseract 方法（上課使用的）
使用這個方式發現辨識出的結果為 2199-QD
https://github.com/janice880624/digital-image-processing/blob/main/HW4/tesseract.py

### muggle 方法
使用這個方式發現辨識出的結果為 2799qd
https://github.com/janice880624/digital-image-processing/blob/main/HW4/muggle.py

### 討論
使用 tesseract 方法辨識出的英文較為準確
使用 muggle 方法辨識出的數字較為準確
所以我結合了兩個方法做出我的成果

大致方法如下：
step1. 將兩種方法得出的結果儲存為陣列
step2. 透過元素的對比得出結果