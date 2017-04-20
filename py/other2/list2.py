#coding:utf8

# 转换函数(sum()/min()/max()等)，对数据做转换或筛选

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print s # 55

# Determine if any .py files exist in a dictionary
import os
dirname = '.'
files = os.listdir(dirname)
if any(name.endswith('.py') for name in files):
    print 'there be python..'
else:
    print 'no python ..'

# output a tuple as CSV
s = ('ACME', 50, 123.45)
print ','.join(str(x) for x in s) # ACME,50,123.45

# data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 70},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 60}
]
min_shares = min(s['shares'] for s in portfolio)
print min_shares # 20
# min_shares = min(portfolio, key=lambda x: x['shares'])['shares'];print min_shares # 20
min_shares = min(portfolio, key=lambda x: x['shares'])
print min_shares # {'name': 'AOL', 'shares': 20}
