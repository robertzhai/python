# -*- coding: utf-8 -*-
import scrapy
from weather.UserAgent import RotateUserAgent
import os
from scrapy.http import Request, FormRequest
import time
import sys
from weather.items import TqItem
import json
from pyv8 import PyV8
import arrow
import copy

class TqSpider(scrapy.Spider):

    name = "tq"
    allowed_domains = ["tianqi.2345.com"]

    js_ctx = None

    # data_api = 'http://tianqi.2345.com/t/wea_history/js/201608/54823_201608.js'
    data_api_first = 'http://tianqi.2345.com/t/wea_history/js/%s/%s_%s.js'
    #http://tianqi.2345.com/t/wea_history/js/54906_20162.js
    data_api_second = 'http://tianqi.2345.com/t/wea_history/js/%s_%s.js'
    code_city = {}

    headers = {
        'Host': 'tianqi.2345.com',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        'Cache-Control': 'no-cache',
        "Pragma": "no-cache",
        "Referer": 'http://tianqi.2345.com',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    def __init__(self):
        self.user_agent = RotateUserAgent.get_user_agent()
        fh =  open(os.getcwd() +  os.sep + 'code_city.txt')
        while True:
            line = fh.readline()
            if not line:
                break
            line = line.split(',')
            if line[1]:
                self.code_city[line[0]] = line[1]
        fh.close()

        #init js_ctx
        ctx = PyV8.JSContext()
        ctx.enter()
        self.js_ctx = ctx

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):

        return [Request(url='http://tianqi.2345.com',
                meta={'cookiejar': 1},
                headers=self.headers,
                callback=self.after_index
                )]

    def after_index(self, response):

        years = ['2015', '2016']
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        '''
        return [Request(url='http://tianqi.2345.com/t/wea_history/js/201608/54823_201608.js',
                meta={'cookiejar': 1},
                headers=self.headers
                )]
        '''
        cur_month = int(arrow.utcnow().month)
        for year in years:

            for month in months:
                if int(month) > cur_month and year == '2016':
                    continue
                for (code, city) in self.code_city.iteritems():
                    if year == '2016' and int(month) >= 3:
                        url = self.data_api_first % (year + month, code, year + month)
                    else:
                        url = self.data_api_second % (code, year + str(int(month)))
                    print url
                    time.sleep(1)
                    headers = copy.deepcopy(self.headers)
                    headers['Referer'] = 'http://tianqi.2345.com/wea_history/%s.htm' % code
                    headers['User-Agent'] = RotateUserAgent.get_user_agent()
                    yield Request(url=url,
                                  meta={'cookiejar': response.meta['cookiejar']},
                                  headers=headers
                                  )

    def parse(self, response):

        json_index = -1
        if response.status == 200:
            data = response.body
            data = data.decode('gbk').encode('utf-8')
            # print data
            json_index = data.find('var weather_str=')

        if response.status == 200 and json_index > -1:
            json_str = data.replace('var weather_str=', '')
            json_str = json_str.strip('; \n')
            if len(json_str) > 0:
                fret = self.js_ctx.eval("""
                                function func() {
                                  var data = """ + json_str + """;
                                  var json_data = JSON.stringify(data);
                                  return json_data;
                                }
                                """)

                jsond = self.js_ctx.locals.func()
                json_data = json.loads(jsond)
                if 'city' in json_data and 'tqInfo' in json_data:
                    tqInfo = json_data['tqInfo']
                    for item in tqInfo:
                        if not item or 'ymd' not in item:
                            continue
                        tq_item = TqItem()
                        tq_item['city'] = json_data['city']
                        tq_item['ymd'] = item['ymd']
                        tq_item['bWendu'] = item['bWendu']
                        tq_item['yWendu'] = item['yWendu']
                        tq_item['tianqi'] = item['tianqi']
                        tq_item['fengxiang'] = item['fengxiang']
                        tq_item['fengli'] = item['fengli']
                        # tq_item['aqi'] = item['aqi']
                        # tq_item['aqiInfo'] = item['aqiInfo']
                        # tq_item['aqiLevel'] = item['aqiLevel']
                        yield tq_item

        else :
            fh = open('log.txt', 'a+')
            fh.write(response.url + ' error , reponse.status:' + response.status + ' \n')
            fh.close()

        yield None

