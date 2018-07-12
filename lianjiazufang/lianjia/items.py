# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaZufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#租房信息标题
    communtiy = scrapy.Field()#居民小区
    rental = scrapy.Field()#租金,元/月
    distance = scrapy.Field()#地铁距离,米
    area = scrapy.Field()#房屋面积,平米
    room_number=scrapy.Field()#几室
    hall_number = scrapy.Field()#几厅
    floor_number =scrapy.Field()#共多少层
    floor_height = scrapy.Field()#楼层高度,高中低
    direction = scrapy.Field()#房屋朝向
    year_build=scrapy.Field()#建造年份


    pass
