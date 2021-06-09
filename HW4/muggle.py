import muggle_ocr
import cv2 as cv

# ModelType.Captcha 可识别4-6位验证码
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
with open(r"output.jpg", "rb") as f:
  b = f.read()
text = sdk.predict(image_bytes=b)

print(text)
