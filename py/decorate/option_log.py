from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined.....')
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('calling ->', func.__name__)
        return func(*args, **kwargs)
    return wrapper

# >>> from option_log import optional_debug
# >>> @optional_debug
# ... def test(a,b,c):
# ...     print(a, b, c)
# ...
# >>> test(1,2,3)
# 1 2 3
# >>> test(1,2,3,debug=True)
# calling -> test
# 1 2 3
