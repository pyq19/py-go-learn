#coding:utf8


# deque 一个双端队列，能在队列两端添加或删除队列元素。
# 支持线程安全，能够有效利用内存
# 无论从队列的哪端入队和出队性能都接近O(1)

import collections

d = collections.deque('ab')
print d # deque(['a', 'b'])

print d.append('c') # None
print d # deque(['a', 'b', 'c'])

d.appendleft('d')
print d # deque(['d', 'a', 'b', 'c'])

d.popleft()
print d # deque(['a', 'b', 'c'])

d.extend('xy')
print d
# deque(['a', 'b', 'c', 'x', 'y'])

d.extendleft('op')
print d
# deque(['p', 'o', 'a', 'b', 'c', 'x', 'y'])

d.rotate(2)
print d
# deque(['x', 'y', 'p', 'o', 'a', 'b', 'c'])

d.rotate(-3)
print d
# deque(['o', 'a', 'b', 'c', 'x', 'y', 'p'])

