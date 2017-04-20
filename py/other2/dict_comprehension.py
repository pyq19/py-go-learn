#coding:utf8

# 字典推导式

# 创建一个字典，其本身是另一个字典的子集

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print prices.items() # [('HPQ', 37.2), ('FB', 10.75), ('AAPL', 612.78), ('IBM', 205.55), ('ACME', 45.23)]
for k, v in prices.items():
    print k
    print v
    # HPQ
    # 37.2
    # ...

# make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
print p1 # {'AAPL': 612.78, 'IBM': 205.55}

# make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key, value in prices.items() if key in tech_names }
print p2 # {'HPQ': 37.2, 'AAPL': 612.78, 'IBM': 205.55}

# 大部分可以用字典推导式解决的问题也可以通过创建元组序列然后将它们传给dict()函数来完成
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print p3 # {'AAPL': 612.78, 'IBM': 205.55}

# p2 还可以重写成
# p4 = { key:prices[key] for key in prices.keys() & tech_names }
# print p4
# Traceback (most recent call last):
#   File "dict_comprehension.py", line 36, in <module>
#       p4 = { key:prices[key] for key in prices.keys() & tech_names }
#       TypeError: unsupported operand type(s) for &: 'list' and 'set'
