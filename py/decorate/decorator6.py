# coding:utf8
# 将装饰器定义为类
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p09_define_decorators_as_classes.html


import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

print(add(2, 5))
# 7

s = Spam()
s.bar(1)
# <__main__.Spam object at 0x102185908> 1

print(Spam.bar.ncalls)
# 1

s.bar(100)
print(Spam.bar.ncalls)
# <__main__.Spam object at 0x1022a08d0> 100
# 2

s.bar(10000)
print(Spam.bar.ncalls)
# <__main__.Spam object at 0x1019a08d0> 10000
# 3
