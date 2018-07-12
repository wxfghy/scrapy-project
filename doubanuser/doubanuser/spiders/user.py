# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from doubanuser.items import userItem
import re

class myspider(scrapy.Spider):
    name = 'user'
    allowed_domains =['movie.douban.com']

    def start_requests(self):
        urlfile=open('D:/neusoft/项目/01分布式爬虫/out/1.txt','r',encoding='utf8')
        all_url = []
        for line in urlfile:
            url=line.split('\t')[1].replace('www','movie')+'collect'
            if url not in all_url:
                all_url.append(url)
        for url in all_url:
            print(url)
            yield Request(url,self.parse)
    def parse(self, response):

        # 看过的电影
        max_page =re.findall(r'(\d+)',BeautifulSoup(response.text, 'lxml').find('span', class_='subject-num').get_text())[-1]

        for num in range(0,int(max_page),15):
            url = response.url+f'?start={num}&sort=time&rating=all&filter=all&mode=grid'
            # 页码加上之后就获得了所有带爬取的URL,调用获取信息的方法
            yield Request(url,callback=self.get_message)
    def get_message(self,response):
        item = userItem()
        content = BeautifulSoup(response.text, 'lxml')
        #每条信息都装在div中,通过class捕获,单页最多30条
        house_list = content.find_all('div', {'class': 'item'})
        for li in house_list:
            item['moviename'] = li.find('li',class_='title').find('a').find('em').get_text()# 电影名
            item['username'] = content.find('div',class_='side-info-txt').find('h3').get_text()# 用户名
            score = li.find_all('span')[0].attrs['class'][0]
            if score == 'playable':
                nscore = li.find_all('span')[1].attrs['class'][0]
                if nscore == 'rating5-t': item['score'] = '5'
                elif nscore == 'rating4-t': item['score'] = '4'
                elif nscore == 'rating3-t': item['score'] = '3'
                elif nscore == 'rating2-t': item['score'] = '2'
                elif nscore == 'rating1-t': item['score'] = '1'
                else: item['score'] = '0'
            else:
                if score == 'rating5-t': item['score'] = '5'
                elif score == 'rating4-t': item['score'] = '4'
                elif score == 'rating3-t': item['score'] = '3'
                elif score == 'rating2-t': item['score'] = '2'
                elif score == 'rating1-t': item['score'] = '1'
                else: item['score'] = '0'
            yield item