#coding:utf8


[x for x in range(10)]              # 列表   
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

{x for x in range(10)}              # 集合    
# set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

{c:ord(c) for c in 'abc'}           # 字典
# {'a': 97, 'c': 99, 'b': 98}

(x for x in range(10))
# <generator object <genexpr> at 0x10b8a4aa0>

[x for x in range(10) if x % 2]
# [1, 3, 5, 7, 9]

['{0}{1}'.format(c, x) for c in 'abc' for x in range(3)]
# ['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']

n = []
for c in 'abc':
    for x in range(3):
        n.append('{0}{1}'.format(c, x))
# print n # ['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']

['{0}{1}'.format(c, x)              \
    for c in 'aBcD' if c.isupper()  \
    for x in range(5) if x % 2      \
]
# ['B1', 'B3', 'D1', 'D3']

def test(it):
    for i, x in enumerate(it):
        print '{0} = {1}'.format(i, x)
test(hex(x) for x in range(3))
# 0 = 0x0
# 1 = 0x1
# 2 = 0x2
