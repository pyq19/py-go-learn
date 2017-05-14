#coding:utf8
class Root(object):
    def __init__(self):
        print 'this is root'

class B(Root):
    def __init__(self):
        print 'this is B, enter B'
        super(B, self).__init__()
        print 'leave B..'

class C(Root):
    def __init__(self):
        print 'enter C'
        super(C, self).__init__()
        print 'leave C'

class D(B, C):
    pass

d = D()
print d.__class__.__mro__
# this is B, enter B
# enter C
# this is root
# leave C
# leave B..
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Root'>, <type 'object'>)
