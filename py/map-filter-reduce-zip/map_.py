# coding:utf8
# https://eastlakeside.gitbooks.io/interpy-zh/content/Map%20&%20Filter/Map.html


# Map 会将一个函数映射到一个输入列表的所有元素上
# map(function_to_apply, list_to_inputs) -> return a list

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print squared
# [1, 4, 9, 16, 25]

squ = map(lambda x: x**2, items)
print squ
# [1, 4, 9, 16, 25]

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items)) # !!!
# python2 中，map 直接返回list
# python3 中，map 返回迭代器, 所以加list(map(...))


print '==' * 20
def multiply(x):
    return (x ** x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in xrange(5):
    value = map(lambda x: x(i), funcs)
    print list(value)
# [1, 0]
# [1, 2]
# [4, 4]
# [27, 6]
# [256, 8]

