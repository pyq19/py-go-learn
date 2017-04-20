#coding:utf8

# 为Class提供装饰器无非是将类型对象作为参数而已

def singleton(cls):
    def wrap(*args, **kw):
        o = getattr(cls, '__instance__', None)
        if not o:
            o = cls(*args, **kw)
            cls.__instance__ = o
        return o
    return wrap


@singleton
class A(object):
    def __init__(self, x):
        self.x = x


print 'A ->', A

print 'a, b = A(1), A(2), a is b ?'
a, b = A(1), A(2)
print a is b

# A -> <function wrap at 0x10d1a0f50>
# a, b = A(1), A(2), a is b ?
# True


def singleton(cls):
    class wrap(cls):
        def __new__(cls, *args, **kw):
            o = getattr(cls, '__instance__', None)
            if not o:
                o = object.__new__(cls)
                cls.__instance__ = 0
            return 0
    return wrap

@singleton
class A(object):
    def test(self): print hex(id(self))

