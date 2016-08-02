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

class SinopecsalesSpider(scrapy.Spider):

    name = "sinopecsales"
    allowed_domains = ["sinopecsales.com"]
    index_url = 'http://www.sinopecsales.com'
    login_submit = 'http://www.sinopecsales.com/websso/loginAction_login.json'
    login_before = 'http://www.sinopecsales.com/websso/loginAction_form.action'

    start_urls = (login_before,)

    def __init__(self):
        self.user_agent = RotateUserAgent.get_user_agent()

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        self.logger.info('Parse function called on start_requests')
        return [Request(url='http://www.sinopecsales.com/websso/YanZhengMaServlet?%s' % random.random(),
                        meta={'cookiejar': 1},
                        callback=self.post_login)]

    def post_login(self, response):
        print '-----Preparing login----'
        code = self.process_image(response)
        print "------code:", code, response.meta['cookiejar']
        data={
              'memberAccount': 'liulin09baidu',
              'memberUmm': hashlib.sha1('hao123456').hexdigest(),
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
        return [FormRequest(url=self.login_submit,
                                        meta={'cookiejar': response.meta['cookiejar'] },
                                        headers=reqheaders,
                                        formdata=data,
                                        callback=self.after_login,
                                        errback=self.errback_httpbin,
                                        dont_filter = True
                                          )]

    def after_login(self, response):

        print response.body, response.meta['cookiejar']
        print 'after_login ..... '
        # holderCardNo=1000113700015449971&priCardNo=1000113700015449964
        cards = {
            '1000113700015701703':'1000113700015701700',
            '1000113700015706220':'1000113700015701700',
            '1000113700015701702':'1000113700015701700',
            '1000113700015701701':'1000113700015701700',
            '1000113700015701704':'1000113700015701700',
            '1000113700015706202':'1000113700015701700',
            '1000113700015706203':'1000113700015701700',
            '1000113700015701705':'1000113700015701700',
            '1000113700015701706':'1000113700015701700',
            '1000113700015706205':'1000113700015701700',
            '1000113700015701707':'1000113700015701700',
            '1000113700015701708':'1000113700015701700',
            '1000113700015706204':'1000113700015701700',
            '1000113700015701709':'1000113700015701700',
            '1000113700015701710':'1000113700015701700',
            '1000113700015706206':'1000113700015701700',
            '1000113700015706207':'1000113700015701700',
            '1000113700015706208':'1000113700015701700',
        }
        for (holderCardNo,priCardNo,) in cards.items():

            # post_data = {
            #     'holderCardNo': '1000113700015449971',
            #     'priCardNo': '1000113700015449964',
            # }
            post_data = {
                'holderCardNo': holderCardNo,
                'priCardNo': priCardNo,
            }
            reqheaders = {
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
                "Referer": 'http://www.sinopecsales.com/gas/webjsp/query/billDetail.jsp',
            }
            print  post_data, '------------ get billQueryAction_compareCard data ..... :'
            yield FormRequest(url='http://www.sinopecsales.com/gas/webjsp/billQueryAction_compareCard.json',
                                meta={'cookiejar': response.meta['cookiejar'], 'holderCardNo': holderCardNo,
                                    'priCardNo': priCardNo},
                                headers=reqheaders,
                                formdata=post_data,
                                callback=self.getViceCardObject
                                )


    def getViceCardObject(self, response):
        #cardMember.cardNo=1000113700015449964&viceCard=1000113700015449971
        post_data = {
            'cardMember.cardNo': response.meta['priCardNo'],
            'viceCard': response.meta['holderCardNo'],
        }
        reqheaders = {
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
            "Referer": 'http://www.sinopecsales.com/gas/webjsp/query/billDetail.jsp',
        }

        print  post_data, '------------ get json data ..... :', response.meta['cookiejar']

        time.sleep(2)
        return [FormRequest(url='http://www.sinopecsales.com/gas/webjsp/billQueryAction_getViceCardObject.json',
                            meta={'cookiejar': response.meta['cookiejar'],'holderCardNo': response.meta['holderCardNo'],
                                    'priCardNo': response.meta['priCardNo']},
                            headers=reqheaders,
                            formdata=post_data,
                            callback=self.transaction_log,
                            )]

    def transaction_log(self, response):
        post_data = {
            'cardMember.cardNo': response.meta['holderCardNo'],
            'startTime': '2016-07-25',
            'endTime': '2016-08-01',
            'traType': 'false',
            'dateFlag': 'true'
        }

        reqheaders = {
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
            "Referer": 'http://www.sinopecsales.com/gas/webjsp/query/billDetail.jsp',
        }
        requrl = 'http://www.sinopecsales.com/gas/webjsp/billQueryAction_transactionLog.json?sjs=%d' % int(
            time.time() * 1000)
        print  post_data, '------------ get billQueryAction_transactionLog data ..... :', requrl, response.meta['cookiejar']

        time.sleep(2)
        return [FormRequest(url=requrl,
                            meta={'cookiejar': response.meta['cookiejar'], 'holderCardNo': response.meta['holderCardNo'],
                                    'priCardNo': response.meta['priCardNo']},
                            headers=reqheaders,
                            formdata=post_data,
                            callback=self.parse,
                            )]

    def parse(self, response):

        print '------------------- in parse -----------'
        json_data = response.body.decode('gbk').encode('utf-8')
        # print 'in parse , response:', json_data
        card_oils = json.loads(json_data)
        if 'list' not in card_oils or  (not card_oils['list']) :
            print 'billQueryAction_transactionLog.json result:', json_data
            yield None
        holders = card_oils['holders']
        card_no = card_oils['no']
        for item in card_oils['list']:
            sinopecsales_item = SinopecsalesItem()
            # sinopecsales_item['holders'] = holders
            sinopecsales_item['cardNo'] = card_no
            sinopecsales_item['amount'] =  '%.2f' % (int(item['amount'])/100.0)
            # sinopecsales_item['balance'] =  '%.2f' % (int(item['balance'])/100.0)
            # sinopecsales_item['litre'] =  '%.2f' % (int(item['litre'])/100.0)
            # sinopecsales_item['price'] =  '%.2f' % (int(item['price'])/100.0)
            # sinopecsales_item['reward'] =  '%.2f' % (int(item['reward'])/100.0)
            # sinopecsales_item['oilName'] = item['oilName']
            sinopecsales_item['opeTime'] = item['opeTime']
            # sinopecsales_item['nodeTag'] = item['nodeTag']
            # sinopecsales_item['traName'] = item['traName']
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
