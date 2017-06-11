# coding:utf8
# https://eastlakeside.gitbooks.io/interpy-zh/content/Map%20&%20Filter/Reduce.html


# 当需要对一个列表进行计算并返回结果时候，
# 如需要计算一个整数列表的乘积时

# from functools import reduce # !!! 可用可不用？
product = reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
print product
# 120
