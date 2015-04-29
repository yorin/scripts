# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImagesearchPipeline(object):
    def process_item(self, item, spider):
        return item
        pass

class HtmlFilePipeline(object):
    def process_item(self, item, spider):
        file_name = hashlib.sha224(item['url']).hexdigest() #chose whatever hashing func works for you
        with open('files/%s.html' % file_name, 'w+b') as f:
            f.write(item['html'])

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
