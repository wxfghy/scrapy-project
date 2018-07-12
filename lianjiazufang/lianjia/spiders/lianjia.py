import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from lianjia.items import LianjiaZufangItem
import requests
import re

class myspider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains =['sy.lianjia.com']

    def start_requests(self):
        theme_url = 'http://sy.lianjia.com/zufang/'
        html = requests.get(theme_url)
        content = BeautifulSoup(html.text, 'lxml')

        urls = []
        links = content.find('div', class_='option-list').find_all('a')#当前城市所有城区的URL链接
        for link in links:
            i = re.findall(r'g/(.*)/', link['href'])
            if i:
                urls.extend(i)
        #所有链接为当前城市各城区的链接集合
        all_url = ['http://sy.lianjia.com/zufang/{}/pg1/'.format(i) for i in urls]
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
        item = LianjiaZufangItem()
        content = BeautifulSoup(response.text, 'lxml')
        #每条信息都装在div中,通过class捕获,单页最多30条
        house_list = content.find_all('div', {'class': 'info-panel'})

        for li in house_list:
            try:
                data = li.find('span', class_='fang-subway-ex').find('span').get_text()
                #这里是地铁信息,默认写法是"距离1号线云峰北街站440米",所以仅提取第二个数字,数字
                item['distance'] = re.findall(r'(\d+)', data)[1]
            except:
                #-1表示租房没有提供地铁信息
                item['distance'] = '-1'
            try:
                #这里是房屋建造年份,数字
                item['year_build'] = re.findall(r'(\d+)', li.find('div', class_='con').get_text().split('/')[-1])[0]
            except:
                #-1表示未提供建造年份信息
                item['year_build'] = '-1'
            item['title'] = li.find('h2').find('a').attrs['title']#租房信息标题,中文
            item['communtiy'] = li.find('span',class_='region').get_text()#所在的居民小区名称,中文
            item['rental'] = li.find('div', class_='price').find('span').get_text()#月租金,默认单位为元/月,数字
            item['area'] = re.findall(r'(\d+)', li.find('span', class_='meters').get_text().replace('&nbsp', ''))[0]#房屋面积,默认单位为平米,数字
            item['room_number'] = re.findall(r'(\d+)',li.find('span', class_='zone').find('span').get_text().replace('\xa0',''))[0]#几室,数字
            item['hall_number'] = re.findall(r'(\d+)',li.find('span', class_='zone').find('span').get_text().replace('\xa0',''))[1]#几厅,数字
            item['floor_number'] = re.findall(r'(\d+)',li.find('div', class_='con').get_text().split('/')[1])[0]  # 总楼层,数字
            item['floor_height'] = re.findall(r'[\u4e00-\u9fa5]', li.find('div', class_='con').get_text().split('/')[1])[0]  # 楼层所在高度,高中低,中文
            item['direction'] = li.find('div', class_='where').find_all('span')[-1].get_text()  # 房屋朝向,中文
            yield item
