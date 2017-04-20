#coding:utf8

print eval('(1 + 2) * 3') # 9

print eval("{'a': 1, 'b': 2}") # {'a': 1, 'b': 2} 将字符串转换为dict

# eval默认会使用当前环境的名字空间，
# 也可以带入自定义字典

x = 100
print eval('x + 200') # 300 使用当前上下文的名字空间

ns = dict(x=10, y=20)
print eval('x + y', ns) # 30 使用自定义名字空间

print ns.keys() # ['y', 'x', '__builtins__']  名字空间里多了__builtins__
