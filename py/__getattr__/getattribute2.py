# coding:utf8
# https://www.bbsmax.com/A/kPzO2qQQdx/


# 新式类的属性访问


# 实例绑定  a.attr
# 类绑定    A.attr
# 实例字典  a.__dict__
# 类字典    A.__dict__
# 类的MRO   A.__mro__   类及其基类组成的序列
# 元类                  用于创建类的类
# 普通属性              不是描述符的属性
# 描述符                存在__get__ __set__ __delete__ 三种特殊方法的任意组合的类的实例
# 数据描述符            定义了__get__ __set__
# 非数据描述符          只定义__get__


#######################
# 获取属性

class A(object): pass
a = A()
# a.attr # 不存在属性attr, 抛出AttributeError 异常
# AttributeError: 'A' object has no attribute 'attr'


class A(object):
    def __getattr__(self, name): # self -> 实例对象a, name -> 实例属性'attr'
        return name + ' in __getattr__ ..'
a = A()
print a.attr # attr in __getattr__ ..
# A 中存在特殊方法__getattr__ ，返回A.__getattr__(a, 'attr')


class A(object):
    attr = 'ordinary attribute in A'
    def __getattr__(self, name):
        return name + ' in __getattr__'
a = A()
print a.attr # ordinary attribute in A
# 类字典A.__dict__ 中存在普通属性attr， 返回A.__dict__['attr']


class Descr(object):
    def __get__(self, instance, owner):
        return 'non-data descriptor in A'

class A(object):
    attr = Descr()
    def __getattr__(self, name):
        return name + ' in __getattr__'
a = A()
print a.attr  # non-data descriptor in A
# 类字典A.__dict__ 中存在非数据描述符attr, 返回Descr.__get__(attr, a, A) # !!! attr?


class Descr(object):
    def __get__(self, instance, owner):
        return 'non-data descriptor in A'

class A(object):
    attr = Descr()
    def __init__(self):
        self.attr = 'attribute in a'
    def __getattr__(self, name):
        return name + ' in __getattr__'
a = A()
print a.attr  # attribute in a
# 实例字典a.__dict__ 中存在属性attr, 返回a.__dict__['attr']


class Descr(object):
    def __get__(self, instance, owner):
        print 'self ->', self
        return 'data descriptor in A'
    def __set__(self, instance, value):
        pass

class A(object):
    attr = Descr()
    def __init__(self):
        self.attr = 'attribute in a'
    def __getattr__(self, name):
        return name + ' in __getattr__'
a = A()
print 'data description ->', a.attr
# 类字典A.__dict__ 中存在数据描述符attr, 返回 Descr.__get__(attr, a, A)
# data description -> self -> <__main__.Descr object at 0x105658450>
# data descriptor in A


class Descr(object):
    def __get__(self, instance, owner):
        return 'data descriptor in A'
    def __set__(self, instance, value):
        pass

class A(object):
    attr = Descr()
    def __init__(self):
        self.attr = 'attribute in a'
    def __getattribute__(self, name):
        return name + ' in __getattribute__'
    def __getattr__(self, name):
        return name + ' in __getattr__'
a = A()
print a.attr
# attr in __getattribute__


