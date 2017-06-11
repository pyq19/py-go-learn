# coding:utf8
# https://www.ziwenxie.site/2017/01/29/python-descriptors/


class RevealAccess(object):
    def __get__(self, obj, objtype):
        print 'self in RevealAccess: {}'.format(self)
        print 'self: {}\nobj: {}\nobjtype: {}'.format(self, obj, objtype)


class MyClass(object):
    x = RevealAccess()
    def test(self):
        print 'self in MyClass: {}'.format(self)


m = MyClass()
m.test()
# self in MyClass: <__main__.MyClass object at 0x104cb5fd0>

print m.x
# self in RevealAccess: <__main__.RevealAccess object at 0x104cb5f90>
# self: <__main__.RevealAccess object at 0x104cb5f90>
# obj: <__main__.MyClass object at 0x104cb5fd0>
# objtype: <class '__main__.MyClass'>
# None

print '==' * 30

print MyClass.x
# self in RevealAccess: <__main__.RevealAccess object at 0x105cfdf90>
# self: <__main__.RevealAccess object at 0x105cfdf90>
# obj: None
# objtype: <class '__main__.MyClass'>
# None


# 如果是对·实例属性·访问，相当于调用了object.__getattribute__()，
# 将obj.x 转译成type(obj).__dict__['x'].__get__(obj, type(obj))

# 如果是对·类属性·进行访问，相当于调用了type.__getattribute__(),
# 将cls.x 转译成cls.__dict__['x'].__get__(None, cls)

def __getattribute__(self, key):
    """Emulate type_getattro() in Objects/typeobject.c"""
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
        return v.__get__(None, self)
    return v


# 描述符优先级
# 描述符分2种，
#   1. 如果同时定义了__get__(), __set__()，则这个描述符称为data descriptor
#   2. 如果只定义了__get__() 方法，则称为non-data descriptor


# 我们对属性进行访问时，存在4种情况
#   1. data descriptor
#   2. instance dict
#   3. non-data descriptor
#   4. __getattr__()
# 优先级1>2>3>4
# 即
# 如果实例对象obj 中，出现了同名的data descriptor -> d
# 和instance attribute -> d
# obj.d 对属性d 进行访问的时候，由于data descriptor 具有更高的优先级，
# python 便会调用type(obj).__dict__['d'].__get__(obj, type(obj))
# 而不是调用obj.__dict__['d']
# 但如果描述符是non-data descriptor， python 则会调用obj.__dict__['d']


print '========='
# Property
# 每次使用描述符的时候都定义一个描述符类非常繁琐，Python提供
# 了一种简洁的方式来向属性添加数据描述符(data-descriptor)
# property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

class Account(object):
    def __init__(self):
        self._acct_num = None

    def get_acct_num(self):
        print ' in get'
        return self._acct_num

    def set_acct_num(self, value):
        self._acct_num = value

    def del_acct_num(self):
        del self._acct_num

    acct_num = property(get_acct_num, set_acct_num, del_acct_num, '_acct_num property.')
# 如果acct是Account的一个实例，acct.acct_num将会调用getter，
# acct.acct_num = value将调用setter，del acct_num.acct_num将调用deleter。

acct = Account()
acct.acct_num = 1000
print acct.acct_num
# in get
# 1000

# @property
class Account(object):
    def __init__(self):
        self._acct_num = None

    # the _acct_num property. the decorator creates a read-only property
    @property
    def acct_num(self):
        return self._acct_num

    # the _acct_num property setter makes the property writeable
    @acct_num.setter
    def set_acct_num(self, value):
        self._acct_num = value

    @acct_num.deleter
    def del_acct_num(self):
        del self._acct_num
# 如果想让属性只读，只需去掉setter 方法


# 在运行时创建描述符
# 即在运行时添加property 属性
# TODO

