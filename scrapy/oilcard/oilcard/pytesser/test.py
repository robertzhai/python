# -*- coding: utf-8 -*-
from pytesser import *
from PIL import Image
from PIL import ImageEnhance
import sys

print image_to_string(Image.open("./training/1.png"))
text = image_file_to_string('./training/1.png', graceful_errors=True)
print text
sys.exit()

im = Image.open('a.jpg')
imgry = im.convert('L')
# imgry.show()

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')

#使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(out)
image_enhancer = enhancer.enhance(4)

print image_to_string(image_enhancer)

sys.exit()


im = Image.open('a.jpg')
text = image_to_string(im)
print "Using image_to_string(): "
print text
text = image_file_to_string('a.jpg', graceful_errors=True)
print "Using image_file_to_string():"
print text
sys.exit()

# text = image_file_to_string('fonts_test.png', graceful_errors=True)
text = image_file_to_string('a.jpg', graceful_errors=True)
print text
sys.exit()
im = Image.open('a.jpg')

enhancer = ImageEnhance.Contrast(im)
image2 = enhancer.enhance(4)
# print image_file_to_string(image2)
print image_to_string(image2)
sys.exit()
imgry = im.convert('L')
# imgry.show()

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()