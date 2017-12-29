# coding=utf-8
# -*- coding: UTF-8 -*-
import sys
from imp import reload
reload(sys)
# sys.setdefaultencoding('utf-8')

import scrapy
import codecs
import json
import os
import urllib



class TOM61(scrapy.Spider):
    name = "tom61"

    def start_requests(self):

        start_url = 'http://www.tom61.com/youxiuzuowen/'
        yield scrapy.Request(url=start_url, callback=self.parse_1)

    def parse_1(self, response):
        a_list = response.xpath('//div[@id="Mhead1_0"]/ul/li/a')
        for a in a_list:
            url = 'http://' + a.xpath('./@href').extract_first()
            category = a.xpath('./text()').extract_first()
            request = scrapy.Request(url, callback=self.parse_2)
            request.meta['category'] = category
            yield request

    def parse_2(self, response):
        category = response.meta['category']
        a_list = response.xpath('//div[@id="Mhead2_0"]/dl[@class="txt_box"]/dd/a')
        for a in a_list:
            url = response.urljoin(a.xpath('./@href').extract_first())
            request = scrapy.Request(url, callback=self.parse_3)
            request.meta['category'] = category
            yield request
        next_page = response.xpath('//div[@class="t_fy"]/a[@class="nextpage"]')[-1]
        if next_page is not None:
            url = next_page.xpath('./@href').extract_first()
            text = next_page.xpath('./text()').extract_first().strip()
            if text == '下一页':
                url = response.urljoin(url)
                request = scrapy.Request(url, callback=self.parse_2)
                request.meta['category'] = category
                yield request

    def parse_3(self, response):
        category = response.meta['category']
        title = response.xpath('//div[@class="t_news"]/h1/text()').extract_first()
        text = '\n'.join(response.xpath('//div[@class="t_news_txt"]/p/text()').extract())
        yield {'category': category, 'title': title, 'url': response.url, 'text': text}


class GZ_YL(scrapy.Spider):
    name = "gzyl"

    def start_requests(self):

        start_urls = [
            'http://www.51test.net/channel_list_more.asp?page=1&classid=17&Nclassid=197&Key=&search_key=%D2%E9%C2%DB%CE%C4&search_key2=%B8%DF%D2%BB',
            'http://www.51test.net/channel_list_more.asp?page=2&classid=17&Nclassid=197&Key=&search_key=%D2%E9%C2%DB%CE%C4&search_key2=%B8%DF%B6%FE',
            'http://www.51test.net/channel_list_more.asp?page=2&classid=17&Nclassid=197&Key=&search_key=%D2%E9%C2%DB%CE%C4&search_key2=%B8%DF%C8%FD',
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_1)

    def parse_1(self, response):
        a_list = response.xpath('//div[@class="news-list-left-content"]/ul/li/a')
        for a in a_list:
            url = a.xpath('./@href').extract_first()
            url = response.urljoin(url)
            title = a.xpath('./text()').extract_first()
            request = scrapy.Request(url, callback=self.parse_2)
            request.meta['title'] = title
            yield request
        center = response.xpath('//div[@class="news-list-left-content"]/ul//form[@class="small14"]/a')
        next_page = None
        for a in center:
            print('---************************************************************************-----------')
            if a.xpath('./text()').extract_first().strip() == '下一页':
                next_page = a.xpath('./@href').extract_first()
                print ('-----------------------------------------------------------------------')
                break
        if next_page is not None:
            url = response.urljoin(next_page)
            url = urllib.quote(url)

            print(url)
            request = scrapy.Request(url, callback=self.parse_1)
            yield request

    def parse_2(self, response):
        content_txt = response.xpath('//div[@class="container"]//div[@class="content-fl"]//div[@class="content-txt"]')
        title = response.meta['title']
        text_list = content_txt.xpath('./p/text()').extract()
        text = '\n'.join(text_list)
        yield {'category': '议论文类', 'title': title, 'url': response.url, 'text': text}


class ZHIKU(scrapy.Spider):
    name = "zhiku"

    def start_requests(self):

        start_urls = [
            # 'http://www.chinathinktanks.org.cn/content/list?id=6&pt=1',
            'http://www.chinathinktanks.org.cn/content/list?id=5&pt=1',
            'http://www.chinathinktanks.org.cn/content/list?id=3&pt=1',
            'http://www.chinathinktanks.org.cn/content/list?id=7&pt=1',
            'http://www.chinathinktanks.org.cn/content/list?id=4&pt=1',
            'http://www.chinathinktanks.org.cn/content/list?id=10&pt=1',
            'http://www.chinathinktanks.org.cn/content/list?id=2&pt=1',
        ]

        for i in range(len(start_urls)):
            yield scrapy.Request(url=start_urls[i], callback=self.parse_1)

    def parse_1(self, response):
        a_list = response.xpath('//div[@class="pub_right "]/div[@class="pub_content"]/ul[@class="list"]/li/a')
        for a in a_list:
            url = a.xpath('./@href').extract_first()
            title = a.xpath('./text()').extract_first().strip(' \n\r')
            request = scrapy.Request(url, callback=self.parse_2)
            request.meta['title'] = title
            yield request

        next_page = response.xpath('//div[@class="pub_right "]/div[@class="paragraph"]//a[@class="next"]')
        if next_page is not None:
            url = next_page[0].xpath('./@href').extract_first()
            url = response.urljoin(url)
            request = scrapy.Request(url, callback=self.parse_1)
            yield request

    def parse_2(self, response):
        title = response.meta['title']
        text_list = []
        p_list = response.xpath('//div[@class="container_mian"]//div[@class="pub_right"]//div[@class="artContent  "]/p')
        for p in p_list:
            text = p.xpath('./text()').extract_first()
            strong = p.xpath('./strong/text()').extract_first()
            if strong is not None:
                text_list.append(strong.strip(' '))
            if text is not None:
                text_list.append(text.strip(' '))

        text = '\n'.join(text_list)
        yield {'category': '议论文类', 'title': title, 'url': response.url, 'text': text}


class GUOKE(scrapy.Spider):
    name = "guoke"

    def start_requests(self):
        #for id in xrange(442005,442006):
        for id in range(439900,449999):
            url = 'https://www.guokr.com/article/' + str(id) +'/'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_1)

    def parse_1(self, response):
        title = response.xpath('//div[@class="container article-page"]//div[@class="content-th"]//h1[@id="articleTitle"]/text()').extract_first()
        document = response.xpath('//div[@class="container article-page"]//div[@class="document"]/div/*')
        print(document)
        print ('------------------------------------------------------------------------------------------------------')
        text_list=[]
        for item in document:
            if item.xpath('./@class').extract_first() == 'img-caption':
                continue
            text_list.append( item.xpath('./text()').extract_first().strip(' /n/r') )
        text='\n'.join(text_list)
        print (text)
        print ('-------------------------------------------------------------------------------------------------------')
        yield {'category':'果壳网科技文','title':title,'url': response.url, 'text': text}

        