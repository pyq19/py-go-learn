#coding:utf8

# 如果一个 类 想被用于for...in循环，类似list/tuple，
# 就必须实现__iter__方法，该方法返回一个 迭代对象，
# 然后for循环就会不断调用该 迭代对象 的__next__方法拿到循环的下个值
# 直到遇到StopIteration退出循环


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a, b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自身

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环的条件
            raise StopIteration
        return self.a # 返回下一个值

    next = __next__ # 兼容Python 2

# >>> from __iter__ import Fib
# >>> for n in Fib():
# ...     print(n)
# ...
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# ...
# 987


if __name__ == '__main__':
    for n in Fib():
        print(n)
