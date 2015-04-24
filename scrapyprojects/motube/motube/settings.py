# -*- coding: utf-8 -*-

# Scrapy settings for motube project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'motube'

SPIDER_MODULES = ['motube.spiders']
NEWSPIDER_MODULE = 'motube.spiders'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'motube (+http://www.yourdomain.com)'

#http://mahmoud.abdel-fattah.net/2012/04/07/using-scrapy-with-proxies/
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'motube.middlewares.ProxyMiddleware': 100,
#}
