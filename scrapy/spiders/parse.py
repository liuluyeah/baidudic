# -*- coding: utf-8 -*-
import os,codecs
import pickle

if __name__ == '__main__':
    word_dict = pickle.load(open("word_dict_2.pk", "rb"))
    word_dict2 = pickle.load(open("word_deleted_2.pk", "rb"))
    print(len(word_dict))
    print(len(word_dict2))
    exit()
    basedir2 = r'D:\KAOLA\py3\baidudic\results\114173_2w'
    files2 = os.listdir(r'D:\KAOLA\py3\baidudic\results\114173_2w')
    for file in files2:
        fd = codecs.open(basedir2 + '\\' + file, 'r', encoding='UTF-8')
        if '抱歉，汉典暂未收录' in fd.read():
            del word_dict[file.split('.')[0]]

    basedir4 = r'D:\KAOLA\py3\baidudic\results\114173_4w'
    files4 = os.listdir(r'D:\KAOLA\py3\baidudic\results\114173_4w')
    for file in files4:
        fd = codecs.open(basedir4 + '\\' + file, 'r', encoding='UTF-8')
        if '抱歉，汉典暂未收录' in fd.read():
            del word_dict[file.split('.')[0]]

    basedir6 = r'D:\KAOLA\py3\baidudic\results\114173_6w'
    files6 = os.listdir(r'D:\KAOLA\py3\baidudic\results\114173_6w')
    for file in files6:
        fd = codecs.open(basedir6 + '\\' + file, 'r', encoding='UTF-8')
        if '抱歉，汉典暂未收录' in fd.read():
            del word_dict[file.split('.')[0]]

    basedir8 = r'D:\KAOLA\py3\baidudic\results\114173_8w'
    files8 = os.listdir(r'D:\KAOLA\py3\baidudic\results\114173_8w')
    for file in files8:
        fd = codecs.open(basedir8 + '\\' + file, 'r', encoding='UTF-8')
        if '抱歉，汉典暂未收录' in fd.read():
            del word_dict[file.split('.')[0]]

    basedir10 = r'D:\KAOLA\py3\baidudic\results\114173_10w'
    files10 = os.listdir(r'D:\KAOLA\py3\baidudic\results\114173_10w')
    for file in files10:
        fd = codecs.open(basedir10 + '\\' + file, 'r', encoding='UTF-8')
        if '抱歉，汉典暂未收录' in fd.read():
            del word_dict[file.split('.')[0]]

    output = open('word_deleted_2.pk', 'wb')
    pickle.dump(word_dict, output)
    output.close()