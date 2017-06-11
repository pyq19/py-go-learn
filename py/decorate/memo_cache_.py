# coding:utf8
# http://docs.pythontab.com/interpy/func_caching/python_2/


from functools import wraps

def memoize(func):
    memo = {}
    @wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv
    return wrapper


@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print fibonacci(25)
