#!/usr/bin/env python
# coding:utf-8

class Date(object):

    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return "{2}年{1}月{0}日".format(self.day, self.month, self.year)
    
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)
    
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date1 = Date('12','11','2014')
date2 = Date.from_string('11-13-2017')

print date1.display()
print date2.display()

print date2.is_date_valid('11-12-2014')
print Date.is_date_valid('11-13-2014')
