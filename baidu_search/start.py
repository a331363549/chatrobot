# -*- coding: utf-8 -*-  

""" 
功能： 启动爬虫
时间：2018.1.31
"""

from scrapy import cmdline

cmdline.execute('scrapy crawl subtitle'.split())