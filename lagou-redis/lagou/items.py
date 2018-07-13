# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ExampleItem(Item):
    # 框架默认字段
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()
    # 自定义字段
    positionName = Field()
    companyFullName = Field()
    companyShortName = Field()
    companySize = Field()
    financeStage = Field()
    district = Field()
    education = Field()
    workYear = Field()
    salary = Field()
    positionAdvantage = Field()


class ExampleLoader(ItemLoader):
    default_item_class = ExampleItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
