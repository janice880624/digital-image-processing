import muggle_ocr
import cv2 as cv

sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
with open(r"output.jpg", "rb") as f:
  b = f.read()
text = sdk.predict(image_bytes=b)

print(text)
