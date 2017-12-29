# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import pandas as pd
import numpy as np
import codecs

if __name__ == '__main__':
    words = pd.read_csv('D:\KAOLA\is_word_1-3\isword_contrast2',sep='\t')
    words = np.array(words)
    # fw= codecs.open('D:\KAOLA\is_word_1-3\handian','a','utf8')
    for i in range(2698,len(words)): #len(words)
        ele = words[i][0]
        # print(ele)
        # exit()
        data = urllib.parse.urlencode({'q':ele}).encode(encoding='UTF8')
        request = urllib.request.Request('http://www.zdic.net/sousuo/', data)
        response = urllib.request.urlopen(request)
        file = response.read()
        if response.code != 200:
            print('error code:'+response.code)
        else:
            if '抱歉'in file.decode('UTF8'):
                print('n')
                # fw.write(ele+'\t'+'n'+'\n')
            else:
                print('y')
                # fw.write(ele+'\t'+'y'+'\n')

