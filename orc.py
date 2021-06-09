import muggle_ocr
import pytesseract
from PIL import Image
import cv2 as cv

tesseract_list = []
muggle_list = []
ans_list =[]
ans = ''

img = cv.imread('photo_video/plate.jfif')

# # get grayscale image
def get_grayscale(image):
  return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# # noise removal
def remove_noise(image):
  return cv.medianBlur(image, 5)

# # thresholding
def thresholding(image):
  return cv.threshold(image, 50, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1] # [1]=image

gray = get_grayscale(img) 
thresh = thresholding(gray)
blur = remove_noise(thresh)

# cv.imshow('img', img)
# cv.imshow('gray', gray)
# cv.imshow('thresh', thresh)
# cv.imshow('blur', blur)
cv.imwrite('photo_video/output.jpg', gray)

text_tesseract = pytesseract.image_to_string(blur)
print(text_tesseract)
text_tesseract = filter(str.isalnum, text_tesseract)

for i in text_tesseract:
  tesseract_list.append(i)

sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
with open(r"photo_video/plate.jfif", "rb") as f:
  b = f.read()
text_muggle = sdk.predict(image_bytes=b)

for i in text_muggle:
  if (i.isalnum()==True):
    muggle_list.append(i)


print('tesseract_list:', tesseract_list)
print('muggle_list:', muggle_list)

for j in range(len(tesseract_list)):
  if tesseract_list[j].isalpha() == True:
    ans_list.append(tesseract_list[j])
  else:
    ans_list.append(muggle_list[j])
print(ans_list)

ans = "".join(ans_list)
print(ans)

# if cv.waitKey(0) & 0xff == 27:
#   cv.destroyAllWindows()  