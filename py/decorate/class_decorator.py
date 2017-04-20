import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r
    return wrapper


class Spam(object):
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1
            
# >>> s = Spam()
# >>> s.instance_method(1000000)
# <class_decorator.Spam object at 0x102a5bf60> 1000000
# 0.08025002479553223
# >>> Spam.class_method(1000000)
# <class 'class_decorator.Spam'> 1000000
# 0.08132314682006836
# >>> Spam.static_method(1000000)
# 1000000
# 0.0800020694732666
