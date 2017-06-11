# coding:utf8
# http://docs.pythontab.com/interpy/decorators/nest_deco_in_func/


# 在函数中嵌入装饰器

from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called\n'
            print log_string
            with open(logfile, 'a') as fi:
                fi.write(log_string)
            return func(*args, **kwargs) 
        return wrapped_function
    return logging_decorator


@logit()
def myfunc1():
    pass


@logit(logfile='func2.log')
def myfunc2():
    pass


if __name__ == '__main__':
    myfunc1()
    myfunc2()
