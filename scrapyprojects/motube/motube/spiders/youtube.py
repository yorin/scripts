# -*- coding: utf-8 -*-
import scrapy
#from motube.items import MotubeItem
str = raw_input("");
class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["youtube.com"]
    start_urls = (
        #'https://www.youtube.com/',
        #'https://www.youtube.com/results?search_query=rush',
        "https://www.youtube.com/results?search_query="+ str,
    )

    def parse(self, response):
        #pass
        for sel in response.xpath('//div/h3'):
            title = sel.xpath('a/@title').extract()
            link = sel.xpath('a/@href').extract()
            #desc = sel.xpath('a/text()').extract()
            print title, link #, desc
