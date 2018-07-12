# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import time

class ProxyMiddleWare(object):
    def process_request(self,request, spider):
        # 将读取到的IP地址写入请求
        proxy = self.get_random_proxy()
        print("尝试IP:"+proxy)
        request.meta['proxy'] = proxy

    def get_random_proxy(self):
        # 从文件中随机读取IP地址,读到就返回
        while 1:
            with open('proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy