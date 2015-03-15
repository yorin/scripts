# -*- coding: utf-8 -*-
import scrapy
from thepiratebay.items import ThepiratebayItem

class ThebigbangtheorySpider(scrapy.Spider):
    name = "thebigbangtheory"
    allowed_domains = ["thepiratebay.se"]
    start_urls = (
        'https://www.thepiratebay.se/tv/9386/',
    )

    def parse(self, response):
        #torrent = ThepiratebayItem()
        #torrent['url'] = response.url
        #first method
        #torrent['name'] = response.xpath("//dd/span/a/text()").extract()
        #torrent['url'] = response.xpath("//dd/span/a/@href").extract()
        #another method
        #torrent = response.xpath('//dd/span/a[contains(@href, text())]')
        #torrent.extract()
        # or
        #torrent = response.xpath("//dd/span/a[contains(@href)]/text()").extract()
        #items = []
        #torrent.append(torrent)
        #return torrent
        #pass
        torrentfiles = response.xpath("//dd/span")
        torrents = []
        for torrentfiles in torrentfiles:
            torrent = ThepiratebayItem()
            torrent ["name"] = torrentfiles.xpath("a/text()").extract()
            torrent ["url"] = torrentfiles.xpath("a/@href").extract()
            torrents.append(torrent)
        return torrents

