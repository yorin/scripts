# -*- coding: utf-8 -*-
import scrapy
from thepiratebay.items import ThepiratebayItem

class ThebigbangtheorySpider(scrapy.Spider):
    name = "thebigbangtheory"
    allowed_domains = ["thepiratebay.se/tv/9386/"]
    start_urls = (
        'https://www.thepiratebay.se/tv/9386//',
    )

    def parse(self, response):
        torrent = ThepiratebayItem()
        #torrent['url'] = response.url
        torrent['name'] = response.xpath("//dd/span/a/text()").extract()
        torrent['url'] = response.xpath("//dd/span/a/@href").extract()
        #items = []
        return torrent
        #pass
