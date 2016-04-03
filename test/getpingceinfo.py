import redis

r = redis.Redis(host='114.215.85.245',port=6379,db=0)

count = 4999
c = 0
pos = 0
neg = 0

while 1:
    print "================",count
    data = r.lindex('pingce-answer',count)
    start = data.find('=')
    v = int(data[(start+1):])
    if v == -1:
        neg = neg + 1
        c = c + 1
    else:
        pos = pos + 1 
        c = c + 1

    count = count - 1
    if count == -1:
        break
print pos,neg,c
