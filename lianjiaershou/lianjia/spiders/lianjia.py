import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from lianjia.items import LianjiaItem
import re

class myspider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains =['sy.lianjia.com']

    def start_requests(self):
        #沈阳
        urls = ['tiexi','heping1','shenhe','hunnan','dadong','huanggu','yuhong','sujiatun','shenbeixinqu']
        #大连
        #urls = ['ganjingzi','shahekou','zhongshan','xigang','gaoxinyuanqu','kaifaqudl','jinzhou']

        #所有链接为当前城市各城区的链接集合
        all_url = ['http://sy.lianjia.com/ershoufang/{}/pg1/'.format(i) for i in urls]
        for url in all_url:
            print(url)
            yield Request(url,self.parse)
    def parse(self, response):
        #从当前页面中解析出最大页码数
        page = BeautifulSoup(response.text, 'lxml').find('div', class_='page-box house-lst-page-box')
        max_page = re.findall('Page":(\d+)."cur', str(page))[0]#"page-data='{"totalPage":24,"curPage":1}'>
        #最后一位是页码,-2切片获取除页码完整URL
        bashurl = str(response.url)[:-2]
        for num in range(1,int(max_page)+1):
            url = bashurl+str(num)+'/'
            #页码加上之后就获得了所有带爬取的URL,调用获取信息的方法
            yield Request(url,callback=self.get_message)
    def get_message(self,response):
        item = LianjiaItem()
        content = BeautifulSoup(response.text, 'lxml')
        #每条信息都装在div中,通过class捕获,单页最多30条
        house_list = content.find_all('div', {'class': 'info clear'})

        for li in house_list:
            try:
                #这里是地铁信息,默认写法是"距离1号线云峰北街站440米",所以仅提取第二个数字,数字
                item['distance'] = re.findall(r'(\d+)', li.find('span', class_='subway').get_text())[1]
            except:
                #-1表示租房没有提供地铁信息
                item['distance'] = '-1'
            try:
                item['year_build'] = re.findall(r'(\d+)', li.find('div', class_='positionInfo').get_text())[1]#房屋建造年份,数字
            except:
                item['year_build'] = '-1'
            try:
                tax = li.find('span', class_='taxfree').get_text()  # 5表示房本满5年,2表示房本满2年,0表示未提供信息
                if tax == '房本满五年':
                    item['tax'] = '5'
                elif tax =='房本满两年':
                    item['tax'] = '2'
            except:
                item['tax'] = "0"
            item['floor_number'] = re.findall(r"(\d+)", li.find('div', class_='positionInfo').get_text())[0]#总楼层数,数字
            try:
                floor_height = re.findall(r'[\u4e00-\u9fa5]', li.find('div', class_='positionInfo').get_text())[0]  # 楼层所在高度,321表示高中低,0表示未提供信息
                if floor_height == '高':
                    item['floor_height'] = '3'
                elif floor_height == '中':
                    item['floor_height'] = '2'
                elif floor_height == '低':
                    item['floor_height'] = '1'
            except:
                item['floor_height'] = '0'
            item['communtiy'] = li.find('div',class_='houseInfo').find('a').get_text()#居民小区名,中文
            try:
                item['room_number'] = re.findall(r'(\d+)', li.find('div', class_='houseInfo').get_text().split(' | ')[-4])[0]  #几室,数字
                item['hall_number'] = re.findall(r'(\d+)',li.find('div', class_='houseInfo').get_text().split(' | ')[-4])[1]  # 几厅,数字
            except:
                item['room_number'] = '-1'
                item['hall_number'] = '-1'
            item['area'] = re.findall('(\d+)',li.find('div', class_='houseInfo').get_text().split(' | ')[-3])[0]#房屋面积,默认单位为平米,数字
            item['direction'] = li.find('div', class_='houseInfo').get_text().split(' | ')[-2]#朝向,中文
            item['decoration'] = li.find('div', class_='houseInfo').get_text().split(' | ')[-1]#精装或简装,中文
            item['unit_price'] = re.findall(r'(\d+)', li.find('div', class_='unitPrice').find('span').get_text())[0]  # 单价,元/平,数字
            item['total_price'] = li.find('div', class_='totalPrice').find('span').get_text()  # 总价,万元,数字
            item['title'] = li.find('div', class_='title').find('a').get_text()  # 标题,中文
            yield item