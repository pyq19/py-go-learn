# coding:utf8
# https://www.programiz.com/python-programming/iterator


class PowTwo:
    ''' Class to implement an iterator of powers of two '''
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    # def __next__(self):
    # TypeError: instance has no next() method
    def next(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = PowTwo(4)

i = iter(a)

print next(i)
# 1

print next(i)
# 2
print next(i)
# 4
print next(i)
# 8
print next(i)
# 16
print next(i)
# StopIteration
