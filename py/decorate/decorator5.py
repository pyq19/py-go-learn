# coding:utf8
# 带可选参数的装饰器
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p06_define_decorator_that_takes_optional_argument.html

# 3

from functools import wraps, partial
import logging

# python2 * 报错？？
def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    print(func.__module__)
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    print(func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('spam!')

print('=' * 20)
print(add(1, 2))

print('=' * 20)
spam()

# __main__
# add
# __main__
# spam
# ====================
# 3
# ====================
# spam
# spam!
