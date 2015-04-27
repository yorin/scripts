# -*- coding: utf-8 -*-

# Scrapy settings for imagesearch project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imagesearch'

SPIDER_MODULES = ['imagesearch.spiders']
NEWSPIDER_MODULE = 'imagesearch.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imagesearch (+http://www.yourdomain.com)'
#USER_AGENT = '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"'
#http://tangww.com/2013/06/UsingRandomAgent/
#http://stackoverflow.com/questions/23152739/how-to-make-scrapy-show-user-agent-per-download-request-in-log
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'imagesearch.middlewares.RotateUserAgentMiddleware': 400,
}

#proxy
#http://pythonr.blogspot.com/2014/04/random-proxy-middleware-for-scrapy.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
#    # Fix path to this module
#    'yourspider.randomproxy.RandomProxy': 100,
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = '/path/to/proxy/list.txt'
