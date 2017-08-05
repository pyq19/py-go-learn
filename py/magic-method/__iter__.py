# coding:utf8
# https://stackoverflow.com/questions/3938927/iterator-iter-function-in-python


class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


class Hello(object):
    def __iter__(self):
        return Counter(10, 20)


if __name__ == '__main__':
    # x = Counter(3, 8)
    # for i in x:
    #     print(i)
        # 可运行在python2    3 4 5 6 7 8
        # python3报Traceback (most recent call last):
        #   File "__iter__.py", line 23, in <module>
        #       for i in x:
        #       TypeError: iter() returned non-iterator of type 'Counter'

    h = iter(Hello())
    for i in h:
        print(i)
    # python3 TypeError: iter() returned non-iterator of type 'Counter'
