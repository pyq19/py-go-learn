# coding:utf8
# http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html
# http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods


# __del__
from os.path import join
class FileObject:
    ''' 给文件对象进行包装从而确认在删除时文件流关闭 '''
    
    def __init__(self, filepath='-', filename='sample.txt'):
        # 读写模式打开一个文件
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


# __eq__(self, other) -> ==
# __ne__(self, other) -> !=
# __lt__(self, other) -> <
# __gt__(self, other) -> >=
class Word(str):
    ''' 存储单词的类，定义比较单词的几种方法'''

    def __new__(cls, word):
        # 使用__new__方法因为str是不可变类型
        # 所以必须在创建时候将它初始化
        if ' ' in word:
            print 'value contains spaces. Truncating to first space.'
            word = word[:word.index(' ')]   # 单词是第一个空格之前的所有字符
        return str.__new__(cls, word)
    # >=
    def __gt__(self, other):
        return len(self) > len(other)
    # <
    def __lt__(self, other):
        return len(self) < len(other)
    # 
    def __ge__(self, other):
        return len(self) >= len(other)
    # 
    def __le__(self, other):
        return len(self) <= len(other)


# __getattr__(self, name) 定义当用户试图获取一个不存在的属性时的行为
class A(object):
    
    def __getattr__(self, name):
        if name == 'no':
            return 'NO!'
        return 'ha?'
# >>> from magicmethods2 import A
# >>> a = A()
# >>> a.a
# 'ha?'
# >>> a.no
# 'NO!'
# >>> ^D


# __setattr__(self, name, value)
# __setattr__ 是一个封装的解决方案，无论属性是否存在，
# 它都允许定义对属性的赋值行为
def __setattr__(self, name, value):
    self.name = value
    # 每当属性被赋值的时候，__setattr__() 会被调用，造成递归调用!

def __setattr__(self, name, value):
    self.__dict__[name] = value # 给类中的属性名分配值
    # 定制特有属性

# 使用super 因为不是所有类都有__dict__ 属性
class AccessCounter:
    '''一个包含计数器的控制权限的类 每当值被改变时计数器会加一'''
    
    def __init__(self, value):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
    # 如果不想让其它属性被访问，可以抛出AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


# __call__
# x() 与 x.__call__() 相同
class Entity:
    '''调用实体来改变实体的位置'''
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        # 改变实体的位置
        self.x, self.y = x, y


# 创建对象的描述器
# 描述去是通过得到，设置，删除的时候被访问的类，也可修改其它的对象
# 构建一个描述器，一个类必须有__get__ / __set__ 其中一个，并且实现__delete__
# __delete__(self, instance) 定义当描述器的值被删除的行为

# 描述器实例：单位转换
class Meter(object):
    '''Descriptor for a meter'''

    def __init__(self, value=0.0):
        self.value = float(value)

    # __get__ 定义当描述器的值被取得的时候的行为,
    # instance 是拥有者对象的一个实例
    # owner 是拥有者类本身
    def __get__(self, instance, owner): 
        return self.value

    # __set__ 定义当描述器值被改变时候的行为
    # instance 是拥有者类的一个实例
    # value 是要设置的值
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    '''Descriptor for a foot'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    '''Class to represent distance holding two descriptors for feet and meters'''
    meter = Meter()
    foot = Foot()


# Pickling
# 储存对象  Pickle 是用来序列化Python 数据结构的模块，在需要暂时存储一个对象时
# （如缓存）
import pickle

data = {'foo': [1, 2, 3],
        'bar': ('Hello', 'world!'),
        'baz': True}
jar = open('simple.txt', 'wb')
pickle.dump(data, jar)  # write the pickled data to the file jar
jar.close()

# unpickle
pkl_file = open('simple.txt', 'rb') # connect to the pickled data
data = pickle.load(pkl_file)        # load it into a variable
print data
pkl_file.close()

# __getinitargs__(self)
# __getnewargs__(self)
# __getstate__(self)
# __setstate__(self, state)

import time

class Slate:
    '''Class to store a string and a changelog, and forget its value when
    pickled.'''

    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        # Change the value. Commit last value to history
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print 'Changelog for Slate object:'
        for k, v in self.history.items():
            print '%s\t %s' % (k, v)

    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank slate" when we unpickle.
        return self.history

    def __setstate__(self, state):
        # Make self.history = state and last_change and value undefined
        self.history = state
        self.value, self.last_change = None, None
