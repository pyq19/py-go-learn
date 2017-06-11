# coding:utf8
# http://docs.pythontab.com/interpy/decorators/logging/


from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + 'was calling'
        return func(*args, **kwargs)
    return with_logging


@logit
def addition_func(x):
    return x + x

print addition_func(100)

# addition_funcwas calling
# 200
