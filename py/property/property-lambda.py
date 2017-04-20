#coding:utf8

class User(object):
    def __init__(self, uid):
        self._uid = uid

    uid = property(lambda o: o._uid) # 只读属性

    name = property(lambda o: o._name, \
                    lambda o, v: setattr(o, '_name', v))


u = User(111)
print 'u = User(111)'

print 'u.uid ->', u.uid

u.name = 'TOM'
print 'u.name = "TOM"'

print 'u.name ->', u.name

print 'set u.uid = 100, ERROR'
u.uid = 100
