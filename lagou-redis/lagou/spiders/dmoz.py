import json
import math

import scrapy
from scrapy.spiders import CrawlSpider, Rule

from lagou.items import ExampleItem


class DmozSpider(CrawlSpider):
    name = 'dmoz'
    allowed_domains = ['www.lagou.com']
    start_urls=['https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false']

    # rules = [
    #     Rule(LinkExtractor(
    #         allow=(r'支持正则表示匹配爬虫域www.lagou.com内所有链接')
    #     ), callback='start_requests', follow=True),
    # ]

    def start_requests(self):
        print('start_requests--------------------------------------------------------')
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false'
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
        print(meta)
        jobnum = meta['content']['positionResult']['totalCount']
        pagedemo=math.ceil(jobnum / 15)
        if pagedemo>30:
            pagenum=30
        else:
            pagenum=pagedemo
        print(f'总页数:{pagenum}')
        url = response.url
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

        item = ExampleItem()
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