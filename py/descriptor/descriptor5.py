# coding:utf8
# https://docs.python.org/2/howto/descriptor.html


class RevealAccess(object):
    """A data descriptor that sets and returns values
        normally and prints a message logging their access.
    """
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'updating', self.name
        self.val = val

class MyClass(object):
    x = RevealAccess(100, 'var "x"')
    y = 5

m = MyClass()
print m.x
# retrieving var "x"
# 100
m.x = 20
# updating var "x"
print m.x
# retrieving var "x"
# 20
print m.y
# 5


# staticmethod  classmethod

class StaticMethod(object);
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


class ClassMethod(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        def newfunc(*args):
            return self.f(klass, *args)
        return newfunc

