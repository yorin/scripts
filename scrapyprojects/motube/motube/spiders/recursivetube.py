# -*- coding: utf-8 -*-
from scrapy.http import Request
from motube.items import MotubeItem
import scrapy

class RecursivetubeSpider(scrapy.Spider):
    name = "recursivetube"
    allowed_domains = ["youtube.com"]
    start_urls = (
       # 'http://www.youtube.com/',
        'https://www.youtube.com/results?search_query=rush',
    )
    def start_requests(self):
      for i in range(5):
        yield Request('https://www.youtube.com/results?search_query=rush&page=' + str(i), self.parse_items)
        print i
    def parse_items(self, response):
        sels = []
        for sel in response.xpath('//div[@class="yt-lockup-content"]/h3[@class="yt-lockup-title"]'):
            datafiles = MotubeItem()
            datafiles["title"] = sel.xpath('a/@title').extract()
            datafiles["url"] = sel.xpath('a/@href').extract()
            sels.append(datafiles)
        return sels
