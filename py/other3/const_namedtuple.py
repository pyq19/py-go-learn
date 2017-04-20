#coding:utf8

# import collections
from collections import namedtuple

Const = namedtuple('_', 'min max')(111, 999)
print(Const.min) # 111
print(Const.max) # 999

Offset = namedtuple('_', 'id name description')(*range(3))
print(Offset.id, Offset.name, Offset.description) # 0 1 2
