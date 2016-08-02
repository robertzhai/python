# -*- coding: utf-8 -*-
import scrapy

class DoubanItem(scrapy.Item):

    name = scrapy.Field()
    total = scrapy.Field()