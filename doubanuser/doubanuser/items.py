# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class userItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moviename = scrapy.Field()# 电影名
    score = scrapy.Field()  # 评分
    username = scrapy.Field()  # 用户名