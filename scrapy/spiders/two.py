# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import pandas as pd
import numpy as np
import codecs,pickle

if __name__ == '__main__':
    # word_dict = pickle.load(open(r'D:\KAOLA\py3\baidudic'+u"\\词语_全难度_dic_utf8.pk", "rb"))
    # word_2={}
    # for ele in word_dict.keys():
    #     if len(ele)==2:
    #         word_2[ele] = word_dict[ele]
    # output = open('word_dict_2.pk', 'wb')
    # pickle.dump(word_2, output)
    # output.close()
    # exit()
    word_dict = pickle.load(open('word_dict_2.pk', 'rb'))
    wr_dir = r'D:\KAOLA\py3\baidudic\results\114173_10w'
    counter = 0
    for ele in word_dict:
        counter += 1
        if counter <= 101925:
            continue
        data = urllib.parse.urlencode({'q':ele}).encode(encoding='UTF8')
        request = urllib.request.Request('http://www.zdic.net/sousuo/', data)
        response = urllib.request.urlopen(request)
        file = response.read()
        # if counter > 80000:
        #     break
        if response.code != 200:
            print('error code:'+response.code)
        else:
            content = file.decode('UTF8')
            fw = codecs.open(wr_dir+'\\'+ele + '.html','w','utf8')
            fw.write(content)
            fw.close()


