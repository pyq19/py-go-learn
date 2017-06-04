# coding:utf8
# http://dongweiming.github.io/python-decorator.html


# 装饰器模式
# 缓存数据到redis 的装饰器

from functools import wraps
from redis import Redis

redis = Redis()

def cached(timeout=5 * 60):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # 以执行函数的参数为键
            key = str(args)
            rv = redis.get(key)
            # 发现缓存过，直接返回
            if rv is not None:
                print 'Has match ->', rv
                return rv
            rv = f(*args, **kwargs)
            redis.setex(key, rv, time=timeout)
            return rv
        return decorated_function
    return decorator


@cached()
def printNumber(num):
    return num


if __name__ == '__main__':
    # 注意列表数据有重复
    for i in [1, 2, 5, 11, 2, 7, 9, 1]:
        print printNumber(i)

# 1
# 2
# 5
# 11
# Has match -> 2
# 2
# 7
# 9
# Has match -> 1
# 1
