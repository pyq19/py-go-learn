# coding:utf8
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p14_capture_class_attribute_definition_order.html


from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('expected ', str(self._expected_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()

class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return '.'.join(str(getattr(self, name)) for name in self._order)

# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.66)
    # print(s.name)
    # GOOG
    # print(s.as_csv())
    # GOOG.100.490.66

    # t = Stock('AAPL', 'a lot', 600.66)
    # TypeError: ('expected ', "<class 'int'>")


# 讨论

# __prepare__() 方法会在开始定义类和它的父类时候被执行
# 必须返回一个映射对象以便在类定义体中被使用到
# 这里通过返回一个OrderedDict 可以很容易捕获定义的顺序

# 如果想构造自己的类字典对象，可以很容易的扩展这个功能，
# 以下方案可以防止重复的定义

from collections import OrderedDict

class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()
    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super().__setitem__(name, value)

class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return NoDupOrderedDict(clsname)

class A(metaclass=OrderedMeta):
    def spam(self):
        pass
    def spam(self):
        pass
    # TypeError: spam already defined in A
    # 重复的定义

# 最后还有一点很重要，就是在 __new__() 方法中
# 对于元类中被修改字典的处理。 尽管类使用了另外一个字典来定义，
# 在构造最终的 class 对象的时候， 我们仍然需要
# 将这个字典转换为一个正确的 dict 实例。
#  通过语句 d = dict(clsdict) 来完成这个效果
