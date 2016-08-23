# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class OilcardPipeline(object):
    def process_item(self, item, spider):
        return item


class IpItemPipeline(object):

    def process_item(self, item, spider):
        return item

class DoubanPipeline(object):

    def process_item(self, item, spider):

        if item['name'] and item['total']:
            return item
        else:
            raise DropItem("Missing name or total in %s " % item )


class SinopecsalesPipeline(object):

    def process_item(self, item, spider):

        if item :

            return item
        else:
            raise DropItem("Missing info in %s " % item )