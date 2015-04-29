# -*- coding: utf-8 -*-
#https://groups.google.com/forum/#!topic/scrapy-users/ZpP7iQliGj0
#http://stackoverflow.com/questions/16044616/downloading-images-in-scrapy
import scrapy
from imagesearch.items import ImagesearchItem
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import random

class FreedigitalphotosSpider(scrapy.Spider):
    name = "freedigitalphotos"
    allowed_domains = ["freedigitalphotos.net"]
    start_urls = (
        'http://www.freedigitalphotos.net/',
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="box-padding-mobile clearfix"]')
        #sites = hxs.select('//div[@class="padding-10-0"]')
        #sites = hxs.select('//div[@class="padding-10-0"]')
        #for site in sites:
          #image_urls = site.select('//img/@src').extract()
          #print image_urls
        for site in sites:
          item = ImagesearchItem()
          image_urls = site.select('//img/@src').extract()
          #item['image_urls'] = ["http://www.freedigitalphotos.net" + x for x in image_urls]
          item['image_urls'] = image_urls
          return item

        #pass
