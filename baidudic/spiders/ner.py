# -*- coding: utf-8 -*-
import os,codecs
import pickle
import spacy
import jieba.posseg as pseg

if __name__ == '__main__':
    word_dict = pickle.load(open("w2_garbage.pk", "rb"))
    for ele in word_dict:
        w = pseg.lcut(ele)
        for i in w:
            print(i.word , i.flag)
    # test_doc = nlp(u"北京冷吗")
    # for ent in test_doc.ents:
    #     print(ent, ent.label_, ent.label)


    # word_dict2 = pickle.load(open("word_deleted_2.pk", "rb"))
    # for ele in word_dict2:
    #     del word_dict[ele]
    # output = open('w2_garbage.pk','wb')
    # pickle.dump(word_dict, output)
    # output.close()
    # print(len(word_dict))
