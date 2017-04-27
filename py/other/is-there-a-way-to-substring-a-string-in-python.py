#coding:utf8

# http://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
# Is there a way to substring a string in Python?
# 取得字字符串的方法

#########################

x = 'hello world!'
print x[2:]     # llo world!
print x[:2]     # he 
print x[:-2]    # hello worl
print x[-2:]    # d!
print x[2:-2]   # llo worl

print 'H-e-l-l-o- -W-o-r-l-d'[::2] # Hello World
