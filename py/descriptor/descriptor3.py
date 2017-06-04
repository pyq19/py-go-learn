# coding:utf8
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p10_using_lazily_computed_properties.html


# 3

# 延迟计算属性
# 将一个只读属性定义成一个property, 只在访问的时候才会计算结果
# 一旦被访问后，结果值被缓存，不用每次都计算
class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance) # !!!
            setattr(instance, self.func.__name__, value)
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area.')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('computing perimeter..')
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)
# 4.0
print(c.area)
# computing area.
# 50.26548245743669
print(c.area)
# 50.26548245743669  # 被缓存

# TODO 讨论
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p10_using_lazily_computed_properties.html
