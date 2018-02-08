# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class BaiduSearchPipeline(object):
    def process_item(self, item, spider):
        return item


class SubtitlePipeline(object):
    def process_item(self, item, spider):
        url = item['url']
        file_name = file_name = url.replace('/','_').replace(':','_')
        fp = open('result/' + file_name, 'wb')
        fp.write(item['body'])
        fp.close()
        return item
