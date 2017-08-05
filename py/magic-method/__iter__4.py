# coding:utf8


class Inner(object):
    def __next__(self):
        return 1


class MyIterableClass(object):
    def __init__(self, little, big):
        self.little = little
        self.big = big
        self.inner = Inner()

    def __iter__(self):
        return self.inner


mi = MyIterableClass(1, 10)
mii = iter(mi)

print(next(mii))
print(next(mii))
print(next(mii))
