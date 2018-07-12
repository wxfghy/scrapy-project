# -*- coding: utf-8 -*-
import json
import math

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from lagou.items import LagouItem

class MovieSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']

    def start_requests(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json?city=北京&needAddtionalResult=false'
        yield scrapy.FormRequest(
            url= url,
            formdata={
                'first': 'true',
                'pn': '1',
                'kd': '机器学习'
            },
            callback=self.get_pagenum,
        )
    def get_pagenum(self,response):
        # 确定总页数
        meta = json.loads(response.body)
        jobnum = meta['content']['positionResult']['totalCount']
        pagedemo=math.ceil(jobnum / 15)
        if pagedemo>30:
            pagenum=30
        else:
            pagenum=pagedemo
        print(f'总页数:{pagenum}')
        url = 'https://www.lagou.com/jobs/positionAjax.json?city=北京&needAddtionalResult=false'
        for num in range(1,pagenum+1):
            yield scrapy.FormRequest(
                url= url,
                formdata={
                    'first': 'true',
                    'pn': str(num),
                    'kd': '机器学习'
                },
                callback=self.get_message,
            )
    def get_message(self,response):
        # json.loads获取json数据列表
        meta=json.loads(response.body)
        print(f'meta:{meta}')

        item = LagouItem()
        joblist = meta['content']['positionResult']['result']
        for job in joblist:
            item['positionName'] = job['positionName']
            item['companyFullName'] = job['companyFullName']
            item['companyShortName'] = job['companyShortName']
            item['companySize'] = job['companySize']
            item['financeStage'] = job['financeStage']
            item['district'] = job['district']
            item['education'] = job['education']
            item['workYear'] = job['workYear']
            item['salary'] = job['salary']
            item['positionAdvantage'] = job['positionAdvantage']

            yield item