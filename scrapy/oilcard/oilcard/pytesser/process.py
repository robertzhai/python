# -*- coding: utf-8 -*-
import urllib
import StringIO
from PIL import Image
import os,random

#存放训练数据
if not os.path.exists('training'):
    os.mkdir('training')

for i in xrange(2):
    #网络上的图片转换成Image对象
    image = Image.open(StringIO.StringIO(urllib.urlopen(
        'http://www.sinopecsales.com/websso/YanZhengMaServlet?%s' % random.random()).read()))
    #灰度化处理
    #有很多种算法，这里选择rgb加权平均值算法
    gray_image = Image.new('L', image.size)
    #获得rgb数据序列，每一个都是(r,g,b)三元组
    raw_data = image.getdata()
    gray_data = []
    for rgb in raw_data:
        value = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
        #value就是灰度值，这里使用127作为阀值，
        #小于127的就认为是黑色也就是0 大于等于127的就是白色，也就是255
        if value < 127:
            gray_data.append(0)
        else:
            gray_data.append(255)
    gray_image.putdata(gray_data)
    gray_image.save(os.path.join('training','%d.png' % i))
    # image.close()
    # gray_image.close()