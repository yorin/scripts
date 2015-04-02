# -*- coding: utf-8 -*-
import scrapy


class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["youtube.com"]
    start_urls = (
        'http://www.youtube.com/',
    )

    def parse(self, response):
        pass
