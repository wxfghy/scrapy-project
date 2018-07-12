# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class movieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()# 用户名
    userurl = scrapy.Field()# 用户URL
    votes = scrapy.Field()  # 影评被点赞数
    score = scrapy.Field()  # 评分