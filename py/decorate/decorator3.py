# coding:utf8
# https://juejin.im/entry/58acfc665c497d005f789fc5


def record(func):
    def wrapper():
        print 'function {} called.'.format(func.__name__)
        func()
    return wrapper

@record
def hi():
    print 'hihi'

@record
def hey():
    print 'heyhey'

hi()
hey()
# function hi called.
# hihi
# function hey called.
# heyhey

###############

from functools import wraps

def record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'func {} called'.format(func.__name__)
        func(*args, **kwargs)
    return wrapper

#########

# 加上返回值
from functools import wraps

def record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'func {} called'.format(func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper


##################

# 装饰器的应用

# 1. 注册函数
# 在以事件模型为处理机制的程序中，经常需要将函数
# 注册到一个API 中，以便对这些函数进行统一的管理

registry = {}
def register(func):
    registry[func.__name__] = func
    return func

# 在需要注册的函数前使用该装饰器
@register
def f1():
    pass

@register
def f2():
    pass

print registry
# {'f1': <function f1 at 0x1044a26e0>, 'f2': <function f2 at 0x1044a2758>}


# 2. 扩展函数
# 例如对函数的信息进行扩展

def add_info(func):
    func.extra_info = 'extra information'
    return func
# 只对原函数添加一个属性返回的还是原函数，因此函数信息不会丢失，无需使用wraps 装饰器

@add_info
def hello(name):
    print 'hello ->', name

print hello.extra_info # extra information


# 3. 日志记录

from functools import wraps

def record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'function <{}> called'.format(func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper

@record
def say_hi():
    print 'hi.........'

say_hi()
# function <say_hi> called
# hi.........


# 4. 计时器

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        elapsed = time.clock() - start
        print '{} executed with {} seconds'.format(func.__name__, elapsed)
        return result
    return wrapper

@timer
def f1(max):
    return [x ** 2 for x in xrange(max)]

@timer
def f2(max):
    return map((lambda x: x ** 2), xrange(max))

f1(10000)
# f1 executed with 0.00098 seconds
f2(10000)
# f2 executed with 0.001715 seconds

# 列表推导式的效率高于map 函数

# TODO 装饰器还有许多其它的应用，例如web应用授权、函数参数合法性验证等等
