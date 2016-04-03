#!/usr/bin/python

import os
import string
import pickle
import pprint


f = open("./lib/negdict.txt")
p = file("./lib/negdict.pkl","w")

posdict = {}
index = 0

while 1:
    index = index + 1
    line = f.readline()
    if line:
    	line = line.replace('\n','')
       	line = line.lstrip()
       	line = line.rstrip()
       	print index, line, len(line)
       	posdict[line] = line
    else:
    	print line
    	break
    	
pickle.dump(posdict,p)
