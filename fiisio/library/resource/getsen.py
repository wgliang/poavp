# -*- coding: UTF-8 -*-
import redis
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
r = redis.Redis(host='114.215.85.245',port=6379,db=0)
count = 4999
pos = open("senpos.txt", "w+")
neg = open("senneg.txt", "w+")
while 1:
    #print "===========",count
    val = r.lindex('pingce-data',count)
    data =  r.lindex('pingce-answer',count)
    start = data.find('=')
    v = int(data[(start+1):])
    print val
    print v
    if v == -1:
        pos.write(val)
        pos.write('\n')
    else:
        neg.write(val)
        neg.write('\n')
    count = count - 1
    if count == -1:
        break
pos.close()
neg.close()

