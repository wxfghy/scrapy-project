# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from doubanmovie.items import movieItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
	# 未登录仅可读取200条,登录后500条
        all_url = ['https://movie.douban.com/subject/26752088/comments?start={}&limit=20&sort=new_score&status=P'.format(i) for i in range(0,500,20)]
        for url in all_url:
            yield Request(url,callback=self.get_message)

    def get_message(self,response):
        item = movieItem()
        content = BeautifulSoup(response.text, 'lxml')
        # 每条信息都装在div中,通过class捕获,单页最多30条
        user_list = content.find_all('div', {'class': 'comment'})
        for li in user_list:
            item['username'] = li.find('span',class_='comment-info').find('a').get_text()# 用户名
            item['userurl'] = li.find('span',class_='comment-info').find('a').attrs['href']# 用户URL
            item['votes'] = li.find('span',class_='votes').get_text()# 影评被点赞数
            score=li.find('span', class_='comment-info').find_all('span')[1].attrs['title']# 评分
            if score == '力荐': item['score'] = '5'
            if score == '推荐': item['score'] = '4'
            if score == '还行': item['score'] = '3'
            if score == '较差': item['score'] = '2'
            if score == '很差': item['score'] = '1'
            yield item