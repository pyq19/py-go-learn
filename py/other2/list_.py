#coding:utf8

# 提取列表中的值，或根据条件对列表删减
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 1 用列表推导式(list comprehension)
print [n for n in mylist if n > 0] # [1, 4, 10, 2, 3]
print [n for n in mylist if n < 0] # [-5, -7, -1]

# 2 生成器表达式 迭代
pos = (n for n in mylist if n > 0)
for x in pos:
    print x
# 1
# 4
# 10
# 2
# 3

# 3 将处理筛选逻辑放入单独函数，并使用内建filter()处理
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print ivals # ['1', '2', '-3', '4', '5']

# ----------------------------------------------------------------------

import math
print [math.sqrt(n) for n in mylist if n > 0] 
# [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
