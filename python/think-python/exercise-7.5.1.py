#! python2
# coding: utf-8

# y = (x + a / x) / 2
def square_root(a,x):
    while True:
        print x
        y = (x + a/x) / 2
        if y == x:
            return y
            break
        x = y
while True:
    a = raw_input('a = '),
    if a == 'q':
        break
    x = raw_input('x = ')
    print 'square_root of a is ',
    print square_root(a, x)
print 'Done!'

