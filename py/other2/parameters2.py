#coding:utf8

def test(a, b):
    print a, b
test(1, 'a') # 1 a

test(b='x', a=100) # 100 x

def test(x, ints=[]):
    ints.append(x)
    return ints
print test(1) # [1]
print test(2) # [1, 2]
print test(3) # [1, 2, 3] # 保持上2次的状态!
print test(1, []) # [1]
print test(3) # [1, 2, 3, 3]


def test(a, b, *args, **kwargs):
    print a, b
    print args
    print kwargs
test(1, 2, 'a', 'b', 'c', x=100, y=200)
# 1 2
# ('a', 'b', 'c')
# {'y': 200, 'x': 100}


def test(*args, **kwargs):
    print args
    print kwargs
test(1, 'a', x='x', y='y')
# (1, 'a')
# {'y': 'y', 'x': 'x'}

test(1)
# (1,)
# {}

test(x='x')
# ()
# {'x': 'x'}


def test(a, b, *args, **kwargs):
    print a, b
    print args
    print kwargs
test(*range(1, 5), **{'x': 'hello', 'y': 'world'})
# 1 2
# (3, 4)
# {'y': 'world', 'x': 'hello'}


def test(a, b):
    print a
    print b
d = dict(a=1, b=2)
test(*d) # 仅展开keys(), test('a', 'b')
# a
# b
test(**d) # 仅展开items(), test(a=1, b=2)
# 1
# 2


test = lambda a, b=0, *args, **kwargs:\
       sum([a, b] + list(args) + kwargs.values())
print test(1, *[2, 3, 4], **{'x': 5, 'y': 6})
# 21
