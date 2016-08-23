# -*- coding: utf-8 -*-
from selenium import webdriver
import StringIO
import random

#获得chrome驱动
browser = webdriver.Chrome()
#打开登录界面
browser.get('http://www.sinopecsales.com/websso/YanZhengMaServlet?%s' % random.random())
#获得截图数据
screen_shot_data = browser.get_screenshot_as_png()
image = Image.open(StringIO.StringIO(screen_shot_data))
#得到验证码区域
#（写死在程序里，并且由于屏幕分辨率不同，不具有通用性）
captcha_img = image.crop((787, 239, 867, 272))

#从文件系统中加载样本数据
trained_data = []
for i in xrange(10):
    trained_data.append([])
    dir = os.listdir(os.path.join('trained','%d'%i))
    for file in dir:
        fn = os.path.join('trained','%d'%i, file)
        img = Image.open(fn)
        trained_data[i].append(list(img.getdata()))
        img.close()

#比较单个数字(算法非常暴力，跟全部样本比较
#并且没有数据大小标准化，选择相同像素最多的作为结果
def _analise(image, trainned_data):
    res = -1
    total_same = 0
    data = list(image.getdata())
    for num in xrange(len(trainned_data)):
        for per_img in trainned_data[num]:
            idx = len(data)
            if idx > len(per_img):
                idx = len(per_img)
            same = 0
            for i in xrange(idx):
                if data[i] == per_img[i]:
                    same += 1
            if same > total_same:
                total_same = same
                res = num
    return str(res)

#分割，比较
def analise(image):
    cimgs = split_image(image)
    res = []
    for cimg in cimgs:
        res.append(_analise(cimg, trainned_data))
        cimg.close()
    image.close()
    return res