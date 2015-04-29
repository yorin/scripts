# -*- coding: utf-8 -*-
#http://www.4byte.cn/question/384709/scrapy-storing-crawled-pages-as-static-files.html
import scrapy
from imagesearch.items import ImagesearchItem

class TesthtmlSpider(scrapy.Spider):
    name = "testhtml"
    allowed_domains = ["www.google.com"]
    def __init__(self, query=None, *args, **kwargs):
      self.start_urls = ['https://www.google.com/search?hl=en&site=imghp&tbm=isch&source=hp&q=%s' % query]


    def parse(self, response):
        item = ImagesearchItem()
        item['html'] = response.body
        item['url'] = response.url
        return item
        #pass
