# -*- coding: utf-8 -*-
import pytesser
import requests
import Image
from StringIO import StringIO
import random
import ImageEnhance
import ImageFilter
from pytesser import *


def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    box = (2, 2, 88, 23)  # 设定裁剪区域

    region = image.crop(box)  # 裁剪图片，并获取句柄region
    return getverify(region)
    # region.save( "crop.jpg" )  # 保存图片

def getverify(im):
    # 二值化
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 由于都是数字对于识别成字母的 采用该表进行修正
    rep = {'O': '0','I': '1', 'L': '1','Z': '2','S': '8','X': '*'};
    # 转化到灰度图
    imgry = im.convert('L')
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    # 识别
    text = image_to_string(out)
    # 识别对吗
    text = text.upper();
    for r in rep:
        text = text.replace(r, rep[r])
        # out.save(text+'.jpg')
    text = text.strip()
    str = eval(text)
    return str

def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

print process_image('http://www.sinopecsales.com/websso/YanZhengMaServlet?%s' % random.random())