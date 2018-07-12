# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):
    def __init__(self):
        self.mfile = open('D:/neusoft/项目/01分布式爬虫/out/userlist.txt','a',encoding='utf8')
    def process_item(self, item,spider):
        username = item['username']
        userurl = item['userurl']
        votes = item['votes']
        score = item['score']
        fstr=f'{username}\t{userurl}\t{votes}\t{score}\n'
        self.mfile.write(fstr)
        return item
    def closefile(self):
        self.mfile.close()