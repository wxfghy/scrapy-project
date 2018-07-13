# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from datetime import datetime

import pandas


class lagouPipeline(object):
    def process_item(self, item, spider):
        # 框架默认
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        # 自定义
        positionName = item['positionName']
        companyFullName = item['companyFullName']
        companyShortName = item['companyFullName']
        companySize = item['companyFullName']
        financeStage = item['companyFullName']
        district = item['companyFullName']
        education = item['companyFullName']
        workYear = item['companyFullName']
        salary = item['companyFullName']
        positionAdvantage = item['companyFullName']
        data=[companyFullName,companyShortName,companySize,financeStage,district,positionName
            ,workYear,education,salary,positionAdvantage]
        columns=['公司全名', '公司简称', '公司规模', '融资阶段', '区域', '职位名称', '工作经验', '学历要求', '工资', '职位福利']
        df=pandas.DataFrame(data=data,index=None,columns=columns)
        df.to_csv('北京-机器学习.csv',index=None)
        return item
