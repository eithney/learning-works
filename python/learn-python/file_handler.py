#!/usr/bin/env python
# _*_ coding: utf-8 _*_


f = open('/tmp/passwd','r')

for i in f.readlines():
    print i.strip('\n').split(':')[3]
