#coding:utf8

import collections

words = ['a', 'b', 'c', 'd', 'e', 'a', 'b']

cnt = collections.Counter(words)
print cnt # Counter({'a': 2, 'b': 2, 'c': 1, 'e': 1, 'd': 1})
print cnt.most_common(3) # [('a', 2), ('b', 2), ('c', 1)]


cnt2 = collections.Counter('asdasdfefg')
print cnt2 # Counter({'a': 2, 'd': 2, 'f': 2, 's': 2, 'e': 1, 'g': 1})

print cnt + cnt2
# Counter({'a': 4, 'd': 3, 'b': 2, 'e': 2, 'f': 2, 's': 2, 'c': 1, 'g': 1})

print cnt - cnt2 # cnt2 相对于cnt计数结果的差集
# Counter({'b': 2, 'c': 1})

print cnt & cnt2 # 两个计数结果的交集
# Counter({'a': 2, 'e': 1, 'd': 1})

print cnt | cnt2 # 两个计数结果的并集
# Counter({'a': 2, 'b': 2, 'd': 2, 'f': 2, 's': 2, 'c': 1, 'e': 1, 'g': 1})
