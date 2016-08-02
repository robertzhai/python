# -*- coding: utf-8 -*-
import pytesser
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
import random


def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    box = (2, 2, 88, 23)  # 设定裁剪区域

    region = image.crop(box)  # 裁剪图片，并获取句柄region

    region.save( "crop.jpg" )  # 保存图片


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

print process_image('http://www.sinopecsales.com/websso/YanZhengMaServlet?%s' % random.random())