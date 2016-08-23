# -*- coding: utf-8 -*-
import scrapy
from oilcard.items import IpItem
from oilcard.UserAgent import RotateUserAgent


# run this spider
# scrapy crawl ip -o ip.json
# scrapy crawl ip -o ip.csv

class IpSpider(scrapy.Spider):

    default_port = 80
    name = "ip"
    allowed_domains = ["ip.cn"]
    start_urls = (
        'http://f.ip.cn/rt/chnroutes.txt',
        'http://f.ip.cn/rt/isproutes-ct.txt',
        'http://f.ip.cn/rt/isproutes-cu.txt'
    )

    def __init__(self):
        self.user_agent = RotateUserAgent.get_user_agent()

    def parse(self, response):
        #xpath to select ip
        for line in response.xpath('*').re(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'):
            ip_item = IpItem()
            ip_item['ip'] = line
            ip_item['port'] = self.default_port
            if ip_item:
                yield ip_item