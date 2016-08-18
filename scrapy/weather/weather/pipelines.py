# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem



class TqPipeline(object):

    def process_item(self, item, spider):

        if item :
            return item
        else:
            raise DropItem("Missing info in %s " % item )