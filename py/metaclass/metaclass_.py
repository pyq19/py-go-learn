# coding:utf8
# https://github.com/xuelangZF/CS_Offer/blob/master/Python/Metaclass.md


# 动态地创建类

def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


MyClass = choose_class('foo')

print MyClass
# <class '__main__.Foo'>

print MyClass()
# <__main__.Foo object at 0x10b0b18d0>

# 当你使用class关键字时，Python解释器自动创建这个对象。
# 但就和Python中的大多数事情一样，Python仍然提供给你手动处理的方法
# type有一种完全不同的能力，它也能动态的创建类。
# type可以接受一个类的描述作为参数，然后返回一个类。

# type(name_of_the_class,
#     tuple_of_the_parent_class(for inheritance, can be empty),
#     dict_containing_attributes_names_and_values)

# 比如 class MyShinyClass(object):
#          pass
# 可以手动创建
MyShinyClass = type('MyShinyClass', (), {})

# type 接受一个字典来为类定义属性，因此class Foo(object):
#                                          bar = True
# 可以翻译为: 
Foo = type('Foo', (), {'bar': 'lalalalala'})

# 类继承： class FooChild(Foo):
#              pass
# 可以写成： 
FooChild = type('FooChild', (Foo,), {})
# print FooChild.bar -> True,   bar 属性由Foo 继承而来

# 为类增加方法
def echo_bar(se):   # se 一般习惯命名为self, 传入的是实例对象
    print se.bar

FooChild = type('FooChild', (Foo,), {'echo': echo_bar})
print hasattr(Foo, 'echo') # False
print hasattr(FooChild, 'echo') # True
my = FooChild()
my.echo() # lalalalala


# 什么是元类
# TODO
