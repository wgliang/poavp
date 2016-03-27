#-*- coding:utf-8 -*-
import urllib2
import requests
import gzip
import StringIO
import ConfigParser
import sys
import time
import re
import redis


        
def getweibo(r,fileObj,uid):
    length = r.llen(uid)
    for i in range(0,length):
        string = r.lindex(uid,i)
        indexl = string.find('weiboinfo:')
        if indexl != -1:
            weibot = string[(indexl+10):]
            indexr = weibot.find(', zan')
            weibo = weibot[0:indexr]
            if weibo.find('href') != -1:
                return 
            else:
                r.lpush('real-weibo', weibo)
                print uid,weibo
    return
    # val = sentiment(string)
    # fileObj.write(val+'\n')
    # return val

def main():
    r = redis.Redis(host='localhost',port=6379,db=0)
    fileObj = open("res.txt", 'a')  
    keys = r.keys("weibo-*")
    for uid in keys:
        getweibo(r, fileObj, uid)
        # print val
    fileObj.close()

if __name__ == "__main__":
    main()