# -*- coding: utf-8 -*-
import scrapy
from oilcard.UserAgent import RotateUserAgent
import sys
from scrapy.selector import Selector
from oilcard.item.DoubanItem import DoubanItem

'''
to get tag and tag ralated total books
run:
scrapy crawl douban -o tag.csv
'''

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://book.douban.com/tag/?view=type&icn=index-sorttags-all',
    )

    def __init__(self):
        self.user_agent = RotateUserAgent.get_user_agent()


    def parse(self, response):
        print response.body
        sel = Selector(text=response.body)
        rows = sel.css('.tagCol').xpath('.//td').extract()
        for line in rows:
            sel = Selector(text=line)
            tag=sel.xpath('//a/text()').extract()
            total=sel.xpath('//b/text()').extract()
            douban_item = DoubanItem()
            douban_item['name'] = tag
            # total = total[0].decode('utf-8')
            douban_item['total'] = total[0].strip('()')
            yield douban_item
