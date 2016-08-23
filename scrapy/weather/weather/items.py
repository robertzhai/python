# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



'''
{ymd:'2016-08-08',bWendu:'29℃',yWendu:'24℃',tianqi:'阵雨',
fengxiang:'北风',fengli:'1-2级',aqi:'48',aqiInfo:'优',aqiLevel:'1'}

{ymd:'2015-05-25',bWendu:'35℃',yWendu:'21℃',tianqi:'晴',fengxiang:'南风',
fengli:'4-5级~3-4级'}


'''
class TqItem(scrapy.Item):

    city = scrapy.Field()
    #日期
    ymd = scrapy.Field()
    #最高气温
    bWendu = scrapy.Field()
    #最低气温
    yWendu = scrapy.Field()
    #天气
    tianqi = scrapy.Field()
    #风向风力
    fengxiang = scrapy.Field()
    fengli = scrapy.Field()
    # #空气质量指数
    # aqi = scrapy.Field()
    # aqiInfo = scrapy.Field()
    # aqiLevel = scrapy.Field()