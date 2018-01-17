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
    name = "tom61wenxue"

    def start_requests(self):

        start_url = 'http://www.tom61.com/ertongwenxue/'
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
        # print(father)
        # exit()
        fw = codecs.open('result2/'+title , 'w' , 'utf8')
        fw.write(text)
        fw.close()
        # yield {'category': category, 'title': title, 'url': response.url, 'text': text}
