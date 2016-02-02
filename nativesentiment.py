# -*- coding: utf-8 -*-
import jieba # 非常不错的强大的中文分析工具
import pickle
import string
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')
posdict = pickle.load(open('./lib/posdict.pkl', 'r'))
negdict = pickle.load(open('./lib/negdict.pkl', 'r'))
mostdict = pickle.load(open('./lib/most.pkl', 'r'))
verydict = pickle.load(open('./lib/very.pkl', 'r'))
moredict = pickle.load(open('./lib/more.pkl', 'r'))
ishdict = pickle.load(open('./lib/ish.pkl', 'r'))
insufficientdict = pickle.load(open('./lib/insufficiently.pkl', 'r'))
inversedict = pickle.load(open('./lib/inverse.pkl', 'r'))

def isOddEven(num):
    if num ^ 1 == 1:
        return 'even'
    else:
        return 'odd'

def segmentation(sentence):
    seg_list = jieba.cut(sentence, True) # 全模式
    # seg_list = jieba.cut(sentence, False) # 精确模式
    # seg_list = jieba.cut_for_search(sentence) # 搜索引擎模式
    # seg_result = ' '.join(seg_list)
    return list(seg_list)

def degreeAward(bite, score):
    ation = 0

    for word in bite:
        k = 0
        for key in mostdict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 1
        for key in verydict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 2
        for key in moredict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 3
        for key in ishdict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 4
        for key in insufficientdict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 5      
        for key in insufficientdict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 6  

        if k == 1:
            score *= 4.0
        elif k == 2:
            score *= 3.0
        elif k == 3:
            score *= 2.0
        elif k == 4:
            score /= 2.0
        elif k == 5:
            score /= 4.0
        elif k == 6:
            ation += 1

    return (score,ation)


def sentiment(sentence):
    words = segmentation(sentence)
    index = 0 # 当前词位置
    senpos = 0 # 上次情感词出现的位置

    posscore = 0 # 积极词得分
    posscore2 = 0 # 积极词得分
    posscore3 = 0 # 积极词得分
    negscore = 0 # 消极词得分
    negscore2 = 0 # 消极词得分
    negscore3 = 0 # 消极词得分
    k = 0

    for word in words:
        for key in posdict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = 1

        for key in negdict:
            key = key.replace('\n','')
            if cmp(key,word) == 0:
                print key,word
                k = -1

        if k == 1:
            posscore = posscore + 1
            (posscore,negation) =  degreeAward(words[senpos:index], posscore)
            if isOddEven(negation) == 'odd':
                posscore *= -1.0
                posscore2 += posscore
                posscore = 0
                posscore3 = posscore + posscore2 + posscore3
                posscore2 = 0      
            else:
                posscore3 = posscore + posscore2 + posscore3
                posscore = 0
            senpos = index + 1
        elif k == -1:
            negscore = negscore + 1
            (negscore,negation) =  degreeAward(words[senpos:index], negscore)
            if isOddEven(negation) == 'odd':
                negscore *= -1.0
                negscore2 += negscore
                negscore = 0
                negscore3 = negscore + negscore2 + negscore3
                negscore2 = 0
            else:
                negscore3 = negscore + negscore2 + negscore3
                negscore = 0
            senneg = index + 1
        elif word == '！'.decode('utf8') or word == '!'.decode('utf8'):
            for w in segtmp[::-1]: #扫描感叹号前的情感词，发现后权值+2，然后退出循环
                if w in posdict or negdict:
                    poscount3 += 2
                    negcount3 += 2
                    break   
        index = index + 1


    pos = 0
    neg = 0
    if posscore3 < 0 and negscore3 > 0:
        neg += negscore3 - posscore3
        pos = 0
    elif negscore3 < 0 and posscore3 > 0:
        pos = posscore3 - negscore3
        neg = 0
    elif posscore3 < 0 and negscore3 < 0:
        neg = -posscore3
        pos = -negscore3
    else:
        pos = posscore3
        neg = negscore3
        
    return  pos,neg

print sentiment("这个手机的质量还不错，尤其是拍照功能,但是这个相机不好,屏幕真是太烂了,非常不满意,很慢，很难用")
