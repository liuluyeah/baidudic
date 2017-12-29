# -*- coding: utf-8 -*-
import pickle,os,math,random
import codecs

if __name__ == '__main__':
    word_dict = pickle.load(open("word_deleted_2.pk", "rb"))
    # slice = random.sample(list(word_dict), 1000)

    # 初级语料 、中级语料、高级语料
    predir = r'D:\KAOLA\corpus\txt0'
    middir = r'D:\KAOLA\corpus\txt1'
    highdir = r'D:\KAOLA\corpus\txt2'

    files0 = os.listdir(predir)
    files1 = os.listdir(middir)
    files2 = os.listdir(highdir)

    output = codecs.open('cifre5w', 'a', 'utf8')
    # output.write('ci'+ '\t' + 'pre'+'\t'+'mid'+'\t'+'high'+'\n')
    cic=0
    for ele in word_dict:
        cic+=1
        if cic <= 15001:
            continue
        counter0 = 0
        for f in files0:
            with open(predir+'\\'+f,'r',encoding='utf8') as fd:
                counter0 += math.log(fd.read().count(ele)+1)

        counter1 = 0
        for f in files1:
            with open(middir+'\\'+f,'r',encoding='utf8') as fd:
                counter1 += math.log(fd.read().count(ele)+1)

        counter2 = 0
        for f in files2:
            with open(highdir+'\\'+f,'r',encoding='utf8') as fd:
                counter2 += math.log(fd.read().count(ele)+1)
        to_w = '\t'.join([ele+word_dict[ele],str(counter0),str(counter1),str(counter2)])
        output.write(to_w+'\n')
    output.flush()
    output.close()