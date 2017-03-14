#!/usr/bin/env python
# coding: utf-8


#print range(10)
#print xrange(10)
#for item in xrange(10):
#    print item
def foo():
    yield 1
    yield 2
    yield 3
    yield 7
    yield 5


re = foo()
for item in re:
    print item
print re

