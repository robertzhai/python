# -*- coding: utf-8 -*-
import scrapy

class SinopecsalesItem(scrapy.Item):

    #{"amount":"20000","balance":"262773","litre":"3160","oilName":"95号车用汽油(V)",
    # "price":"633","opeTime":"2016-07-27 09:10:37",
    # "reward":"200","nodeTag":"滨州石油第5加油站","traName":"加油"}
    # holders = scrapy.Field()
    cardNo = scrapy.Field()
    amount = scrapy.Field()
    # balance = scrapy.Field()
    # litre = scrapy.Field()
    # oilName = scrapy.Field()
    # price = scrapy.Field()
    opeTime = scrapy.Field()
    # reward = scrapy.Field()
    # nodeTag = scrapy.Field()
    traName = scrapy.Field()
