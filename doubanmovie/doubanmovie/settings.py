# -*- coding: utf-8 -*-

# Scrapy settings for doubanmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanmovie'

SPIDER_MODULES = ['doubanmovie.spiders']
NEWSPIDER_MODULE = 'doubanmovie.spiders'
# 重试次数,次和连接超时时间,秒
RETRY_ENABLE = True
RETRY_TIMES = 10
DOWNLOAD_TIMEOUT = 5
#USER_AGENT ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanmovie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# 爬取的间隔,秒,越长越好避免被封
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'Accept':'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
	# 登录账号cookie的话可以读取500条影评
    #'Cookie':'ll="118123"; bid=g9g5V_4Vzus; __yadk_uid=9y8RdakBuTo4xajicD3zD6A236PQv40W; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1531309911%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; ps=y; dbcl2="180953715:bl5PPxnhFc0"; ck=-t27; _vwo_uuid_v2=DC6FF00D53E453DF1EA72A9071B487AFF|269c1b43a678a01763528efe80af1bf7; _pk_id.100001.4cf6=b46cc379520e18cb.1531035508.3.1531310277.1531227603.; _pk_ses.100001.4cf6=*; __utma=30149280.1699850972.1531227595.1531227595.1531309945.2; __utmb=30149280.0.10.1531309945; __utmc=30149280; __utmz=30149280.1531309945.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utma=223695111.953343906.1531035508.1531227598.1531309945.3; __utmb=223695111.0.10.1531309945; __utmc=223695111; __utmz=223695111.1531309945.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; push_noty_num=0; push_doumail_num=0',
    'Host':'movie.douban.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubanmovie.middlewares.DoubanmovieSpiderMiddleware': 543,
#}
# 挂中间件就是使用代理IP
SPIDER_MIDDLEWARES = {
    'doubanmovie.middlewares.ProxyMiddleWare':1000
}
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doubanmovie.middlewares.DoubanmovieDownloaderMiddleware': 543,
#}
# 挂中间件就是使用代理IP
DOWNLOADER_MIDDLEWARES = {
    'doubanmovie.middlewares.ProxyMiddleWare':1000
}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'doubanmovie.pipelines.DoubanmoviePipeline': 300,
#}
ITEM_PIPELINES = {
    'doubanmovie.pipelines.DoubanmoviePipeline': 1000,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

