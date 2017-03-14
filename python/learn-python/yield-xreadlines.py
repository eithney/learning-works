#!/usr/bin/env python
# coding: utf-8

def my_xReadLines():
    seek = 0
    while True:
        with open('/tmp/tmp-read.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return
print my_xReadLines()
for item in my_xReadLines():
    print item
