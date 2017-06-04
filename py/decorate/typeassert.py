# coding:utf8
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p07_enforcing_type_check_on_function_using_decorator.html

# python cookbook
# 利用装饰器强制函数类型检查
# 实现如下效果

# @typeassert(int, int)
# def add(x, y):
#     return x + y

# >>> add(2, 3)
# 5
# >>> add(2, 'hello')
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "contract.py", line 33, in wrapper
# TypeError: Argument y must be <class 'int'>


# 实现

from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # if in optimized mode, disable type checking
        if not __debug__:
            return func

        # map function argument names to supllied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

spam(1, 2, 3)
# 1, 2, 3

spam(1, 'hello', 3)
# 1 hello 3

spam(1, 'hello', 'world')
# Traceback (most recent call last):
#   File "typeassert.py", line 60, in <module>
#     spam(1, 'hello', 'world')
#   File "typeassert.py", line 44, in wrapper
#     'argument {} must be {}'.format(name, bound_types[name])
# TypeError: argument z must be <class 'int'>


# 讨论

# >>> from inspect import signature
# >>> def spam(x, y, z=42):
# ...     pass
# ...
# >>> sig = signature(spam)
# >>> print(sig)
# (x, y, z=42)
# >>> sig.parameters
# mappingproxy(OrderedDict([('x', <Parameter at 0x10077a050 'x'>),
# ('y', <Parameter at 0x10077a158 'y'>), ('z', <Parameter at 0x10077a1b0 'z'>)]))
# >>> sig.parameters['z'].name
# 'z'
# >>> sig.parameters['z'].default
# 42
# >>> sig.parameters['z'].kind
