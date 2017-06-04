# coding:utf8
# 定义一个带参数的装饰器
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p04_define_decorator_that_takes_arguments.html

# 3


from functools import wraps
import logging


def logged(level, name=None, message=None):
    '''
    add logging to a function.
    level is the logging level.
    name is the logger name.
    message is the log message.
    if the name and message are't specified.
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('spam..')

print(add(1, 10))

spam()

# 11
# spam
# spam..
