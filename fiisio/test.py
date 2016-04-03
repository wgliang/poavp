# -*- coding: utf-8 -*-
import fiisio
import redis
r = redis.Redis(host='114.215.85.245',port=6379,db=0)

right = 0
i = 4999
while 1:
    val = r.lindex('pingce-data',i)
    da = r.lindex('pingce-answer',i)
    start = da.find('=')
    ans = str(da[(start+1):])
    if val != None:
        print val
        print "=============",i
        s = fiisio.Fiisio(val)
        num = s.sentiment
        print val,num
        r.lpush('result-pingce',str(num))
	if num - 0.5 > 0.0001:
	    if int(ans) ==  1:
	        right = right + 1
	else:
	    if int(ans) == -1:
		right = right + 1
    i = i -1
    if i == -1:
        break
print right
# from library import normal
# from library import segmentation
# from library import tagger
# from library import sentiment 
# from library import bm25
# from library import frequence
# from library import merger
# from library import model
# from library import segger
# from library import textrank
# from library import tnt
# from library import trie

# sentiment.train('./library/resource/neg.txt', './library/resource/pos.txt')
# sentiment.save('sentiment.marshal')

# s = fiisio.Fiisio(u'加油吧，其实还是支持你的，好好磨练一下演技，拿作品说话吧')        

# s.sentences

#  分词
# s.words         # [u'这个', u'东西', u'真心',
                #  u'很', u'赞']
# for i in range(len(s.words)):
#   print s.words[i]

# 词性标注
# s.tags          # [(u'这个', u'r'), (u'东西', u'n'),
                #  (u'真心', u'd'), (u'很', u'd'),
                #  (u'赞', u'Vg')]
# for i,v in s.tags:
#   print i,v

# 关键词提取
# s.keywords

# 情感分析
# v = s.sentiment
# print v

# ------------------------------------------------------------
