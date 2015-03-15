# -*- coding: utf-8 -*-
import scrapy


class SimpsonsSpider(scrapy.Spider):
    name = "simpsons"
    allowed_domains = ["thepiratebay.se"]
    start_urls = (
        'https://thepiratebay.se/tv/9386',
    )

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        pass
