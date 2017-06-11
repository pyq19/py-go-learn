# coding:utf8
# https://eastlakeside.gitbooks.io/interpy-zh/content/Lambdas/


add = lambda x, y: x + y

print add(1, 2) # 3 


# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print a.sort(key=lambda x: x[1])
# None
print a
# [(13, -3), (4, 1), (1, 2), (9, 10)]
a.sort(key=lambda x: x[0])
print a
# [(1, 2), (4, 1), (9, 10), (13, -3)]


print '--' * 20
# 列表并行排序
from random import randint
list1 = [randint(0, 100) for _ in xrange(10)]
list2 = [randint(0, 100) for _ in xrange(10)]
print 'list1 ->', list1
print 'list2 ->', list2
data = zip(list1, list2)
print 'data ->', data
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
# !!!
