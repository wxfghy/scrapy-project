# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class userPipeline(object):
    def __init__(self):
        self.mfile = open('d:/neusoft/项目/01分布式爬虫/out/score.txt','a',encoding='utf8')
    def process_item(self, item,spider):
        username = item['username']
        moviename = item['moviename']
        score = item['score']
        fstr = f'{username}\t{moviename}\t{score}\n'
        self.mfile.write(fstr)
        return item
    def closefile(self):
        self.mfile.close()