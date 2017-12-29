# -*- coding: utf-8 -*-
import pickle, os, pandas
import numpy as np
# pk_dir = r'D:\KAOLA\is_word_1-3'
# word_dic_pk = pk_dir + "\\is_word_1-3.pk"  # 词语难度字典
# word_dict = pickle.load(open(word_dic_pk, "rb"))
# write_dir = r'D:\KAOLA\is_word_1-3'
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__=="__main__":

    ie_driver = os.path.abspath(r"D:\Applications\IEDriverServer_X64\IEDriverServer.exe")
    os.environ["webdriver.ie.IEDriverServer"] = ie_driver
    browser = webdriver.Ie(ie_driver)
    # browser = webdriver.Chrome(chromedriver)
    # browser = webdriver.Chrome()
    browser.get('http://www.zdic.net/')
    assert "汉典" in browser.title
    elem = browser.find_element_by_id("q")
    elem.send_keys("考拉")
    elem.send_keys(Keys.RETURN)
    result = browser.find_element_by_class_name("notice")
    # result = browser.find_element_by_xpath("//div[@class='notice']/h3/text()")
    print(result.text)

    time.sleep(20)
    browser.close()
    exit()
    word_dict = pandas.read_csv(r'D:\KAOLA\is_word_1-3\isword_contrast2', sep='\t')
    word_dict = np.array(word_dict)
    for i in range(len(word_dict)):
        print(word_dict[i][0])
    exit()


    listfile = os.listdir(r'D:\KAOLA\py3\baidudic\results\no_word_1-3')
    notword=[]
    count=0
    for ele in word_dict:
        if word_dict[ele]=='n':
            notword.append(ele)
    for file in listfile:
        if file in notword:
            notword.remove(file)
            count+=1
    print(len(notword))
    for ele in notword:
        print(ele)
    print(count)
