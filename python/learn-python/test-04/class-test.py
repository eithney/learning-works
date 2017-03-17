#!/usr/bin/env python
# coding:utf-8

class A(object):
    
    _g = 6

    def foo(self,x):
        print('executing foo(%s,%s)' % (self, x))

    @classmethod
    def class_foo(cls,x):
        print('executing class_foo(%s,%s)' % (cls, x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % (x))
a = A()
a.foo(315)

a.class_foo(34)
A.class_foo(34)

a.static_foo(1)
A.static_foo(1)

print a.foo


print a.class_foo

print a.static_foo

print A._g
