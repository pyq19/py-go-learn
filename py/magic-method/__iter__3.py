# coding:utf8
# https://docs.python.org/dev/howto/functional.html#iterators


l = [1, 2, 3] # iterable 可迭代对象

it = iter(l)  # 调用可迭代对象的__iter__ 方法，返回iterator 迭代器

it.__next__() # 与 next(it) 一样


# Python 2      def next(self):
# Python 3      def __next__(self):
