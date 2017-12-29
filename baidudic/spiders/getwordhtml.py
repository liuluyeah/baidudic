# -*- coding: utf-8 -*-
import scrapy,pickle


class GetwordhtmlSpider(scrapy.Spider):
    name = 'getwordhtml'
    # allowed_domains = ['baiduci.io']
    start_urls = []

    def __init__(self):

        word_dict = pickle.load(open(r"D:\KAOLA\py3\baidudic\is_word_1-3.pk", "rb"))
        for ele in word_dict:
            if len(ele) != 2:
                continue
            url = 'http://dict.baidu.com/s?wd=' + ele + '&ptype=empty'
            self.start_urls.append(url)

        # url = 'http://dict.baidu.com/s?wd=长期&ptype=empty'
        # self.start_urls.append(url)

    def parse(self, response):
        isword = response.xpath('//div[@class="tab-content"]/span/text()').extract()
        write_dir = r'D:\KAOLA\py3\baidudic\results\no_word_1-3'
        if len(isword) != 0:
            fname = response.xpath('//title/text()').extract()[0].split("_")[-1]
            with open(write_dir + '\\' + fname , 'wb') as fw:
                fw.write(response.body)
            self.log('saved file %s' % fname)
        pass
