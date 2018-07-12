# -*- coding: utf-8 -*-



from lianjia import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class LianjiaPipeline(object):
    def __init__(self):
        self.mfile = open('沈阳二手房.txt','a',encoding='utf8')
    def process_item(self, item, spider):
        title = item['title']
        communtiy = item['communtiy']
        distance = item['distance']
        area = item['area']
        room_number = item['room_number']
        hall_number = item['hall_number']
        floor_number = item['floor_number']
        floor_height = item['floor_height']
        direction = item ['direction']
        year_build = item['year_build']
        decoration = item['decoration']
        unit_price = item['unit_price']
        total_price = item['total_price']
        tax = item['tax']

        fstr=f'{title}\t{communtiy}\t{floor_height}\t{direction}\t' \
             f'{decoration}\t{area}\t{room_number}\t{hall_number}\t{floor_number}\t' \
             f'{distance}\t{year_build}\t{unit_price}\t{total_price}\t{tax}\n'
        self.mfile.write(fstr)
        return item
    def closefile(self):
        self.mfile.close()
