#coding:utf8
# implement __getitem__ in a class allows its instances to use the `[]`(编索引的，分度器) operators.


class Test(object):
    def __getitem__(self, items):
        print '%-15s  %s' % (type(items), items)

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t['a': 'z': 3]
t[object()]
# <type 'int'>     1
# <type 'str'>     hello world
# <type 'tuple'>   (1, 'b', 3.0)
# <type 'slice'>   slice('a', 'z', 3)
# <type 'object'>  <object object at 0x1035b50f0>


class Indexer:
    def __getitem__(self, index):
        return index ** 2
x = Indexer()
print x[2]      # x[i] calls __getitem__(x, i)
for i in xrange(5):
    print x[i]
# 4
# 0
# 1
# 4
# 9
# 16
