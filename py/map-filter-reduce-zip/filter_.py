# coding:utf8
# https://eastlakeside.gitbooks.io/interpy-zh/content/Map%20&%20Filter/Filter.html


# filter 过滤列表中的元素，并返回一个由所有符合要求的元素所构成的列表
# ·符合要求·即函数映射到该元素时返回值为True 

number_list = xrange(-5, 5)
print list(number_list)
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
less_than_zero = filter(lambda x: x < 0, number_list)
print list(less_than_zero)
# [-5, -4, -3, -2, -1]
