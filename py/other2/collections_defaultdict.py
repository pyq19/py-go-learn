#coding:utf8


import collections

# defaultdict 简化了处理不存在的键的场景

# 如果不使用defaultdict，对一个单词的计数要这样实现

d = {}

words = ['a', 'b', 'c', 'a', 'd', 'c']

for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
print d # {'a': 2, 'c': 2, 'b': 1, 'd': 1}


# 如果使用defaultdict，就不需要判断字典中是否已经存在此键
d = collections.defaultdict(int)
for w in words:
    d[w] += 1
print d # defaultdict(<type 'int'>, {'a': 2, 'c': 2, 'b': 1, 'd': 1})


# defaultdict 参数就是值的类型，还可以使用自定义类型。
# 例如插入后自动排序的自定义列表类型
import bisect
class bisectedList(list):
    def insort(self, arr):
        bisect.insort_left(self, arr)
d = collections.defaultdict(bisectedList)
d['l'].insort(1)
d['l'].insort(9)
d['l'].insort(3)
print d['l'] # [1, 3, 9]


# defaultdict对于不同的数据结构都有默认值，比如int的默认值是0
d = collections.defaultdict(int)
print d['a'] # 0
# 如果想使用其他默认值，可以借用匿名函数lambda来实现
d = collections.defaultdict(lambda x=10: x)
print d['a'] # 10
d['b'] = 1
print d['b'] # 1

