# -*- coding: utf-8 -*-
import scrapy
from imagesearch.items import ImagesearchItem

class ImagedownloadSpider(scrapy.Spider):
    name = "imagedownload"
    allowed_domains = ["www.google.com"]
    def __init__(self, query=None, *args, **kwargs):
      self.start_urls = ['https://www.google.com/search?hl=en&site=imghp&tbm=isch&source=hp&q=%s' % query]

    def parse(self, response):
        item = ImagesearchItem()
        item['images'] = response.body
        item['image_url'] = response.url
        return item
        pass
