# -*- coding: utf-8 -*-
import scrapy,pickle,os


class GetwordhtmlSpider(scrapy.Spider):
    name = 'getwordhtml2'
    # allowed_domains = ['baiduci.io']
    start_urls = []
    # word_dict = {}

    def __init__(self):

        word_dict = pickle.load(open(u"词语_全难度_dic_utf8.pk", "rb"))
        word_dict = os.listdir(r"D:\KAOLA\py3\baidudic\results\not2word")
        for ele in word_dict:
            # if len(ele) != 4:
            #     continue
            url = 'http://dict.baidu.com/s?wd=' + ele + '&ptype=empty'
            self.start_urls.append(url)

        # url = 'http://dict.baidu.com/s?wd=长期&ptype=empty'
        # self.start_urls.append(url)

    def parse(self, response):

        write_dir = r'D:\KAOLA\py3\baidudic\results\not2word2'
        # fname = response.xpath('//title/text()').extract()[0].strip()
        # with open(write_dir + '\\' + fname , 'wb') as fw:
        #     fw.write(response.body)
        # self.log('saved file %s' % fname)
        # word_dict = pickle.load(open(u"词语_全难度_dic_utf8.pk", "rb"))

        isword = response.xpath('//div[@class="tab-content"]/span/text()').extract()

        if len(isword) != 0 :
            ele = response.xpath('//title/text()').extract()[0].split("_")[-1]
            with open(write_dir + '\\' + ele , 'wb') as fw:
                fw.write(response.body)
            self.log('saved file %s' % ele)
            # del self.word_dict[ele]
            # print(ele)

        pass

    # f = open(u"/词语过滤_全难度_dic_utf8.pk", 'wb')
    # pickle.dump(word_dict, f)
    # f.close()
