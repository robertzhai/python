# -*- coding: utf-8 -*-
import scrapy
import requests
import Image
from StringIO import StringIO
import random
import ImageEnhance
import ImageFilter
from oilcard.lib.pytesser.pytesser import *
import hashlib
from scrapy.http import Request, FormRequest
import sys, time

from oilcard.UserAgent import RotateUserAgent
from oilcard.item.SinopecsalesItem import SinopecsalesItem
import json
import string
import time

class SinopecsalesSpider(scrapy.Spider):

    name = "sinopecsales"
    allowed_domains = ["sinopecsales.com"]
    index_url = 'http://www.sinopecsales.com'
    login_submit = 'http://www.sinopecsales.com/websso/loginAction_login.json'
    login_before = 'http://www.sinopecsales.com/websso/loginAction_form.action'

    start_urls = (login_before,)

    def __init__(self,*args, **kwargs):
        super(SinopecsalesSpider, self).__init__(*args, **kwargs)
        self.user_agent = RotateUserAgent.get_user_agent()

        #主卡
        self.main_card = kwargs['main_card']
        # 副卡
        self.second_card = kwargs['second_card']
        print self.main_card, self.second_card

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        self.logger.info('Parse function called on start_requests')
        return [Request(url='http://www.sinopecsales.com/websso/YanZhengMaServlet?%s' % random.random(),
                        meta={'cookiejar': 1},
                        callback=self.post_login)]

    # login request
    def post_login(self, response):
        print '-----Preparing login----'
        code = self.process_image(response)
        print "------code:", code, response.meta['cookiejar']
        data={
              'memberAccount': '*****',
              'memberUmm': hashlib.sha1('*****').hexdigest(),
              'check': str(code),
              'rememberMe': 'on'
        }
        reqheaders =  {
            'Host': 'www.sinopecsales.com',
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
            "Connection": "keep-alive",
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'http://www.sinopecsales.com',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Referer": self.login_before
        }
        time.sleep(5)
        return [FormRequest(url=self.login_submit,
                                        meta={'cookiejar': response.meta['cookiejar'] },
                                        headers=reqheaders,
                                        formdata=data,
                                        callback=self.after_login,
                                        errback=self.errback_httpbin,
                                        dont_filter = True
                                          )]

    def after_login(self, response):
        time.sleep(5)
        print response.body, response.meta['cookiejar']
        print 'after_login ..... '

    def parse(self, response):
        #省略了一些逻辑
        print '------------------- in parse -----------'
        json_data = response.body.decode('gbk').encode('utf-8')
        # print 'in parse , response:', json_data
        card_oils = json.loads(json_data)
        if 'list' not in card_oils or  (not card_oils['list']) :
            print 'billQueryAction_transactionLog.json result:', json_data
            # 打开一个文件
            fo = open("/wwwroot/scrapy/oilcard/log.txt", "a+")
            fo.write('main_card:' + self.main_card + ',second_card:' + self.second_card);
            fo.write('billQueryAction_transactionLog.json result:' + json_data + "\n");
            # 关闭打开的文件
            fo.close()
            yield None
        holders = card_oils['holders']
        card_no = card_oils['no']
        for item in card_oils['list']:
            if item['traName'] == u'加油':
                sinopecsales_item = SinopecsalesItem()
                # sinopecsales_item['holders'] = holders
                sinopecsales_item['cardNo'] = card_no
                sinopecsales_item['amount'] =  '%.2f' % (int(item['amount'])/100.0)
                # sinopecsales_item['litre'] =  '%.2f' % (int(item['litre'])/100.0)
                # sinopecsales_item['price'] =  '%.2f' % (int(item['price'])/100.0)
                # sinopecsales_item['reward'] =  '%.2f' % (int(item['reward'])/100.0)
                # sinopecsales_item['oilName'] = item['oilName']
                sinopecsales_item['opeTime'] = item['opeTime']
                # sinopecsales_item['nodeTag'] = item['nodeTag']
                sinopecsales_item['traName'] = item['traName']
                # print sinopecsales_item
                yield sinopecsales_item



    def errback_httpbin(self, failure):
        print ' in errback_httpbin =========='
        # log all failures
        print failure

    def errback_oil_card(self, failure):
        print ' in errback_oil_card =========='
        # log all failures
        print failure

    def process_image(self, response):
        image = Image.open(StringIO(response.body))
        # image.show()
        image.filter(ImageFilter.SHARPEN)
        box = (2, 2, 88, 23)  # 设定裁剪区域
        region = image.crop(box)  # 裁剪图片，并获取句柄region
        return self.getverify(region)
        # region.save( "crop.jpg" )  # 保存图片

    def getverify(self, im):
        # 二值化
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 由于都是数字对于识别成字母的 采用该表进行修正
        rep = {'O': '0', 'I': '1', 'L': '1', 'Z': '2', 'S': '8', 'X': '*'};
        # 转化到灰度图
        imgry = im.convert('L')
        # 二值化，采用阈值分割法，threshold为分割点
        out = imgry.point(table, '1')
        # 识别
        text = image_to_string(out)
        # 识别对吗
        text = text.upper();
        # print text
        for r in rep:
            text = text.replace(r, rep[r])
            # out.save(text+'.jpg')
        text = text.strip()
        str = eval(text)
        return str


    def get_image(self, response):
        return Image.open(StringIO(response.body)).show()
        # return Image.open(StringIO(requests.get(url).content))
