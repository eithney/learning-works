#!/usr/bin/env python
# coding:utf-8

class Province:
    # static
    describe = '中国的23个省之一'

    
    def __init__(self, name, brieflyname, capital, city, **kw):
        #dynamic
        self.Name = name
        self.BrieflyName = brieflyname
        self.Capital = capital
        self.City = city
        for k, w in kw.iteritems():
            setattr(self, k, w)
        

    def construction(self):
        print self.Name + '正在建设'

    @staticmethod
    def Foo():
        print '坚持可持续发展战略'

    @property
    def Foo1(self):
        print self.Name,'property'

heilongjiang = Province('黑龙江', '黑', '哈尔滨', ['齐齐哈尔', '牡丹江', '佳木斯'], postid='150000')
print heilongjiang.Name,
print Province.describe
print '简称:',heilongjiang.BrieflyName
print '省会:',heilongjiang.Capital
print '主要城市:',
for city in heilongjiang.City:
    print city,
print ''
print '邮政编码:',heilongjiang.postid
heilongjiang.construction()
Province.Foo()
heilongjiang.Foo1
