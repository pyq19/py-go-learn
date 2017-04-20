#coding:utf8

import copy

x = object()

l = [x] # 创建一个对象

l2 = copy.copy(l) # 浅复制，仅复制对象自身，而不会递归复制其成员

print l2 is l # False, 复制列表的元素依然是原对象

print l2[0] is x # True

l3 = copy.deepcopy(l) # 深度复制，会递归复制所有深度成员

print l3 is l # False 列表元素也被复制了

print l3[0] is x # False

