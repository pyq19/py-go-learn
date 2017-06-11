# coding:utf8
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p09_create_new_kind_of_class_or_instance_attribute.html

# 创建新的类或实例属性


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# 为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中。例如：

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# 当你这样做后，所有对描述器属性(比如x或y)
# 的访问会被 __get__() 、__set__() 和 __delete__() 方法捕获到。例如：

p = Point(2, 3)
print(p.x)
# 2
print(p.y)
# 3

# p.x = 2.3
# TypeError: Expected an int


# 讨论

# 描述器可以实现大部分Python 类特性中的底层魔法,
# 包括@classmethod, @staticmethod, @property, __slots__

# 描述器只能在类级别被定义，不能为每个实例单独定义。
# 下面代码无法工作
# class Point:
#     def __init__(self, x, y):
#         self.x = Integer('x') # err, must be a class variable
#         self.y = Integer('y')
#         self.x = x
#         self.y = y


class Integer:
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
# __get__() 看起来复杂归结于实例变量和类变量不同
# 如果一个描述器被当作类变量来访问，那instance 参数被设置成None.
# 这种情况下，标准做法就是简单的返回这个描述器本身即可(尽管你还可以添加其他的自定义操作)
p = Point(2, 3)
print(p.x)     # Calls Point.x.__get__(p, Point) # !!!
# 2
print(Point.x) # Calls Point.x.__get__(None, Point) # !!!
# <__main__.Integer object at 0x102aa06a0>


print('-----------------' * 2)
# 描述器 类型检查
# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            print(instance.__dict__)
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock(name='asd', shares=11, price=1.1)
print(s.name)
# {'name': 'asd', 'shares': 11, 'price': 1.1}
# asd

print('=' * 30)
# print(hasattr(s, 'name')) # True
print(getattr(s, 'name'))
print('=' * 30)

s = Stock(**{'name': 'HHH', 'shares': 321, 'price': 2.2})
print(s.name)
# {'name': 'HHH', 'shares': 321, 'price': 2.2}
# HHH

s = Stock(name=1, shares='as', price='a')
# TypeError: expected <class 'str'>
