# Scrapy settings for lagou project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'

#USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
# 本地重复过滤
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 计划调度器,将请求队列处理分发
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否将本地请求队列持久化到远程服务器
SCHEDULER_PERSIST = True
# 使用框架提供的队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"# 常用,优先级队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"# FIFO队列,先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"# LIFO队列,后进先出

ITEM_PIPELINES = {
    'lagou.pipelines.lagouPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
# 日志级别
# LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 爬取间隔
DOWNLOAD_DELAY = 30

# 请求头
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
# COOKIES不用
COOKIES_ENABLED = False
# 机器人规则不遵守
ROBOTSTXT_OBEY = False

# 重试
RETRY_ENABLE = True
RETRY_TIMES = 5 # 重试次数,次
DOWNLOAD_TIMEOUT = 5 # 超时时长,秒

# 连接远程redis服务,可连接redis集群实现分布式
REDIS_HOST = '10.25.34.65'
REDIS_PORT = 6379