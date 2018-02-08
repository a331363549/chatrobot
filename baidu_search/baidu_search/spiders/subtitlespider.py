# -*- coding: utf-8 -*-  

""" 
功能： 爬取字幕文件
时间： 2018.2.1
"""

import scrapy
from w3lib.html import remove_tags
from baidu_search.items import SubtitleCrawlerItem


class SubTitlesSpider(scrapy.Spider):
    name = 'subtitle'
    allower_domains = ['zimuku.net']
    start_urls = [
            "http://www.zimuku.cn/search?q=&t=onlyst&p=1",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=2",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=3",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=4",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=5",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=6",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=7",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=8",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=9",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=10",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=11",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=12",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=13",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=14",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=15",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=16",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=17",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=18",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=19",
            "http://www.zimuku.cn/search?q=&t=onlyst&p=20",


    ]

    def parse(self, response):
        hrefs = response.selector.xpath('//div[contains(@class,"persub")]/h1/a/@href').extract()
        for href in hrefs:
            url = response.urljoin(href)
            request = scrapy.Request(url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        url = response.selector.xpath('//li[contains(@class,"dlsub")]/div/a/@href').extract()[0]
        print('processing:', url)
        request = scrapy.Request(url, callback=self.parse_file)
        yield request

    def parse_file(self, response):
        item = SubtitleCrawlerItem()
        item['url'] = response.url
        item['body'] = response.body
        return item
