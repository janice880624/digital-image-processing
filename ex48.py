import pytesseract
import cv2 as cv

image = cv.imread('photo_video/plate.jfif')
# img = cv.imread('plate2.jpg')
# text = pytesseract.image_to_string(img)
# print(text)

# # get grayscale image
def get_grayscale(image):
  return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# # noise removal
def remove_noise(image):
  return cv.medianBlur(image,5)

# # thresholding
def thresholding(image):
  return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1] # [1]=image

gray = get_grayscale(image) 
thresh = thresholding(gray)
blur = remove_noise(thresh)



cv.imshow('car plate',blur)
text = pytesseract.image_to_string(blur)
print(text)

if cv.waitKey(0) & 0xff == 27:
  cv.destroyAllWindows()  