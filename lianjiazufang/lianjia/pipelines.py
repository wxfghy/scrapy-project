# -*- coding: utf-8 -*-



from lianjia import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class LianjiaZufangPipeline(object):
    def __init__(self):
        self.mfile = open('沈阳租房.txt','a',encoding='utf8')
    def process_item(self, item, spider):
        title = item['title']
        communtiy = item['communtiy']
        rental = item['rental']
        distance = item['distance']
        area = item['area']
        room_number = item['room_number']
        hall_number = item['hall_number']
        floor_number = item['floor_number']
        floor_height = item['floor_height']
        direction = item ['direction']
        year_build = item['year_build']
        fstr=f'{title}\t{communtiy}\t{floor_height}\t{direction}\t{rental}\t{area}\t{room_number}\t{hall_number}\t{floor_number}\t{distance}\t{year_build}\n'
        self.mfile.write(fstr)
        return item
    def closefile(self):
        self.mfile.close()
