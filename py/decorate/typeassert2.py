# coding:utf8
# https://stackoverflow.com/questions/15299878/how-to-use-python-decorators-to-check-function-arguments

# @check_arguments(types = ['int', 'float'])
# def my_function(this_var_is_an_int, this_var_is_a_float)
#     pass

# 2

# def accepts(*types):
#     def check_accepts(func):
#         assert len(types) == func.func_code.co_argcount
#         def new_func(*args, **kwargs):
#             for (a, t) in zip(args, types):
#                 assert isinstance(a, t), \
#                     'arg %r does not match %s' % (a, t)
#             return func(*args, **kwargs)
#         new_func.func_name = func.func_name
#         return new_func
#     return check_accepts
# 
# 
# @accepts(int, (int, float))
# def func(arg1, arg2):
#     return arg1 * arg2

# print func(3, 2)
# print func('aa', 6)
# print func('as', 'fd')


#############
# 3

# import inspect
# 
# def validate(func):
#     def wrapper(*args):
#         fname = func.__name__
#         fsig = inspect.signature(func)
#         vars = ', '.join('{}={}'.format(*pair) for pair in zip(fsig.parameters, args))
#         params = {k: v for k, v in zip(fsig.parameters, args)}
#         print('wrapped call to {}({})'.format(fname, params))
#         for k, v in fsig.parameters.items():
#             p = params[k]
#             msg = 'call to {}({}): {} failed {})'.format(fname, vars, k, v.annotation.__name__)
#             assert v.annotation(params[k]), msg
#         ret = func(*args)
#         print(' returning {} with annotation: "{}"'.format(ret, fsig.return_annotation))
#         return ret
#     return wrapper
# 
# @validate
# def xXy(x: lambda _x: 10 < _x < 100, y: lambda _y: isinstance(_y.float)) -> ('x times y', 'in X and Y units'):
#     return x * y
# 
# xy = xXy(10, 3)
# print(xy)

# AssertionError: call to xXy(x=10, y=3): x failed <lambda>)

########################


def enforce(*types):
    def decorator(f):
        def new_f(*args, **kwargs):
            # we need to convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a)) # feel free to have more elaborated onvertion
            return f(*newargs, **kwargs)
        return new_f
    return decorator

@enforce(int, float)
def func(arg1, arg2):
    return arg1 * arg2

print(func(3, 2))
print(func('a', 3))
# ValueError: invalid literal for int() with base 10: 'a'
