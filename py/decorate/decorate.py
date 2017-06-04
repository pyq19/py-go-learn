# coding:utf8
# http://python.jobbole.com/87089/


import json
import functools

def json_output(func):
    @functools.wraps(func) # !!!
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return inner


def json_output2(indent=None, sort_keys=False):
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return actual_decorator

@json_output2(indent=4)
def f():
    return {'status': 'done'}

print f()

def json_output3(decorated_=None, indent=None, sort_keys=False):
    if decorated_ and (indent or sort_keys):
        raise # !!!

    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs)
            result = func(*args, **kwargs)
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    
    if decorated_:
        return actual_decorator(decorated_)

    return actual_decorator

@json_output(indent=4)
def f1():
    return {'status': 'done'}
 
@json_output
def f2():
    return {'status': 'done'}
 
@json_output()
def f3():
    return {'status': 'done'}
    
