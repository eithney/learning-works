#!/usr/bin/env python
# _*_ coding: utf-8 _*_


item = ('cellphone', 'bicycle', 'television', 'beer')
cost          = ( 2300      ,  550     ,  4500       ,  30   )
money = input('how much money do you have?')
while money >= cost[item.index('beer')]:
    j = 0
    for i in item:
        print i,  'cost', cost[j], '$'
        j += 1
else:
    print "you can't affort to buy anything here!"
