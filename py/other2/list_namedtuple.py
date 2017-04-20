#coding:utf8

# 将名称映射到序列的元素中

# 通过名称来访问元素

# collection.nametuple() 命名元组，工厂方法，返回标准元组的子类

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('pyq225@gmail.com', '2017-4-13')
print sub # Subscriber(addr='pyq225@gmail.com', joined='2017-4-13')
print sub.addr # pyq225@gmail.com
print sub.joined # 2017-4-13
print len(sub) # 2
addr, joined = sub
print addr, '--', joined # pyq225@gmail.com -- 2017-4-13


# 1
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# 2
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
ll = [['aaa', 111.222, 333.555], ['bb', 2.2, 3.3]]
print compute_cost(ll)
print compute_cost2(ll)
# 37105.91421
# 37105.91421
