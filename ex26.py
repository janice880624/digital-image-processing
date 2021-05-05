import cv2
img = cv2.imread("photo_video/lena.jpg")
print(img.shape) # (512, 512, 3)

print("""
  Zoom In-Out demo
  ------------------
  * [i] -> Zoom [i]n
  * [o] -> Zoom [o]ut
  * [ESC] -> Close program
  """)

while True:
  rows, cols, _channels = map(int, img.shape)
  cv2.imshow('Pyramids Demo', img)
  k = cv2.waitKey(0)
  if k == 27:
    break 
  elif chr(k) == 'i':
    img = cv2.pyrUp(img, dstsize=(2 * cols, 2 * rows))
    print ('** Zoom In: Image x 2')
  elif chr(k) == 'o':
    img = cv2.pyrDown(img, dstsize=(cols // 2, rows // 2))
    print ('** Zoom Out: Image / 2')
cv2.destroyAllWindows()