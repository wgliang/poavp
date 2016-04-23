# -*- coding: utf-8 -*-
import fiisio
import redis

r = redis.Redis(host='114.215.85.245',port=6379,db=0)
count = 2723
rpos = 0
rneg = 0
right = 0
A = 0
B = 0
C = 0
D = 0

while 1:
    #print "===========",count
    #val = r.lindex('pingce-data',count)
    if count == 3456:
        count = count - 1
        continue
    val = r.lindex('comments-papi',count)
    print val
    if val != None:
        #print vali
        s = fiisio.Fiisio(val)
        num = s.sentiment
        print num
        r.lpush('result-papi',str(num))
        if num > 0.5:
            A = A + 1
            if num > 0.51:
                B = B + 1
                right = right + 1
        else:
            C = C + 1
            if num < 0.49:
                right = right + 1
                D = D + 1
    count = count - 1
    if count == -1:
        break
#print A,B-A,C-D,D,right
fo = open("res.txt", "a+")
fo.write( "\nres:  num > 0.51 < 0.49:" + ","+str(A) +","+ str(B) +","+ str(C) +","+ str(D)+","+ str(right)+"\n\n")
fo.close()


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
