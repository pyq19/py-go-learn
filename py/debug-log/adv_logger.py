#coding:utf8

# http://coolshell.cn/articles/11265.html

import inspect
from functools import wraps


def advance_logger(loglevel):
    
    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno # !!!

    def _basic_log(fn, result, *args, **kwargs):
        print 'function ->', fn.__name__
        print 'args -> {args}\nkwargs -> {kwargs}'.format(args=args,kwargs=kwargs)
        print 'return -> {}'.format(result)

    def info_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            _basic_log(fn, result, args, kwargs)
        return wrapper

    def debug_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            _basic_log(fn, result, args, kwargs)
            print 'time ->', (te-ts)
            print 'called_from_line ->', str(get_line_number())

    if loglevel is 'debug':
        return debug_log_decorator
    else:
        return info_log_decorator
