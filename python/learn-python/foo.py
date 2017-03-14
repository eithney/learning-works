#!/usr/bin/env python
# coding: utf-8
'''
def foo(name, action='act', where='yard'):
    print name,'does', action,'@',where

foo('john',where='farm',action='plant')
'''
def show(**kargs):
    for item in kargs.items():
        print item

user_dict = {'k1':123, 'k2':567}

show(**user_dict)

#def showlist(**kargs):
#    for item in kargs.items():
#        # pretty display style
#        print item
#    print '\n'
#
#showlist(name='mary', age=28)

'''
def showlist(*arg):
    for item in arg:
        # pretty display style
        print item,
    print '\n'

showlist(['mary', 'tom'])
showlist(['mary', 'tom'], 'jack')
showlist('mary', 'tom')
'''
