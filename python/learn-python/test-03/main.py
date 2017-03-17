#!/usr/bin/env python
# coding: utf-8
#import os
import pickle

data = {'name':'jack', 'id':3421}

pStr =  pickle.dumps(data)
print pStr
lStr = pickle.loads(pStr)
print lStr
with open('saved.pk','w') as fp:
    pickle.dump(data, fp)
with open('saved.pk','r') as fp:
    lStr1 = pickle.load(fp)
print lStr1
#import time
#print time.time()
#print time.gmtime()
#print time.strftime('%Y-%m-%d %H:%M:%S')
#import re
#ip = '12.34.43.dsfa.234rs~2343242d3343f192.168.32.43_w323d~!@94898'
##print re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
##print re.findall('[0-9]{1,3}(?:\.\d+){1,3}', ip)
#print re.findall('(?:\d{1,3}\.){3}\d{1,3}', ip)
from module import demo
#str1 = 'asdfs245dfs5555dfssf4444237dd'
#re4 = re.search('(\d+)d_ff(\d+)x(\d+)','246d_ff345x89' )
#print re4.group()
#print re4.groups()
#re5 = re.search('a{3,5}', 'aiaajaaak')
#print re5.group()

#re3 = re.findall('\d+', str2)
#if re3:
#    print re3
#else:
#    print 'None'
#com = re.compile('\d+')
#print type(com)
#print com.findall(str2)
#re1 = re.match('\d+', str)
#if re1:
#    print re1.group()
#else:
#    print 'Nothing'
#re2 = re.search('\d+', str)
#if re2:
#    print re2.group()
#else:
#    print 'None'
newList = [11, 22, 33]
#def foo(arg):
#    if arg < 22:
#        return True
#    else:
#        return False


#print divmod(9,4)
#print bool(-1)
#print pow(2,3)

# =====apply=====
#def foo(arg):
#    print arg
#
#foo(3)
#apply(foo, '4')
# ===============

# ===== map =====
#def foo(arg):
#    return arg + 100
#newList = [11, 22, 33]
#tempList = []
#for item in newList:
#    foo(item)
#    tempList.append(foo(item))
#print tempList

#tempList = map(foo,newList)
#print tempList

#tempList =map(lambda arg:arg+100, newList)
#print tempList
