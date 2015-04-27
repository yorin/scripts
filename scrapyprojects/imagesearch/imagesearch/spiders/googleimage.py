# -*- coding: utf-8 -*-
import scrapy


class GoogleimageSpider(scrapy.Spider):
    name = "googleimage"
    allowed_domains = ["www.google.com"]
    def __init__(self, query=None, *args, **kwargs):
#      start_urls = (
#          #'https://www.google.com/search?hl=en&site=imghp&tbm=isch&source=hp&q=bugatti+veyron',
#          'https://www.google.com/search?hl=en&site=imghp&tbm=isch&source=hp&q=%s' % query,
#      )
      self.start_urls = ['https://www.google.com/search?hl=en&site=imghp&tbm=isch&source=hp&q=%s' % query]

    def parse(self, response):
        #print response.url
        #torrentfiles = response.xpath("//div")
        #torrent.extract()
        #torrents = []
        #for torrentfiles in torrentfiles:            
        #    torrent = ThepiratebayItem()
        #    torrent ["name"] = torrentfiles.xpath("a/text()").extract()
        #    torrent ["url"] = torrentfiles.xpath("a/@href").extract()
        #    torrents.append(torrent)
        #return torrents
        #return torrentfiles
        #pass
       for sel in response.xpath('//div[@class="rg_di rg_el"]'):
            #title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            #desc = sel.xpath('text()').extract()
            #print title, link, desc
            print link
