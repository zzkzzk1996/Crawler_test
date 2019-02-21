import pytesseract
from PIL import Image

img = Image.open('test.png')
code = pytesseract.image_to_string(img)
print(code)