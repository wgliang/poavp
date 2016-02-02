# -*- coding: utf-8 -*-
import jieba # 非常不错的强大的中文分析工具
import pickle
import string

posdict = pickle.load(open('./lib/posdict.pkl', 'r'))
negdict = pickle.load(open('./lib/negdict.pkl', 'r'))
mostdict = pickle.load(open('./lib/most.pkl', 'r'))
verydict = pickle.load(open('./lib/very.pkl', 'r'))
moredict = pickle.load(open('./lib/more.pkl', 'r'))
ishdict = pickle.load(open('./lib/ish.pkl', 'r'))


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
    return seg_list

def degreeAward(bite, score):
    negation = 0

    for b in bite:
        if b in mostdict:
            score *= 4.0
        elif b in verydict:
            score *= 3.0
        elif b in moredict:
            score *= 2.0
        elif b in ishdict:
            score /= 2.0
        elif b in insufficientdict:
            score /= 4.0
        elif b in inversedict:
            ation += 1

    return score,ationr


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

    for word in words:
        if word in posdict:
            posscore = posscore + 1
            posscore,negation =  degreeAward(words[senpos:index])
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
        elif word in negdict:
            negscore = negscore + 1
            negscore,negation =  degreeAward(words[senneg:index])
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

    print posscore, negscore
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

print sentiment("这个手机的质量还不错 极佳 极好，尤其是拍照功能")
