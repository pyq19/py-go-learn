# aoding:utf8
# http://code.activestate.com/recipes/454322-type-checking-decorator/


def require(arg_name, *allowed_types):
    def make_wrapper(func):
        if hasattr(func, 'wrapped_args'):
            wrapped_args = getattr(func, 'wrapped_args')
        else:
            code = func.func_code
            wrapped_args = list(code.co_varnames[:code.co_argcount])

        try:
            arg_index = wrapped_args.index(arg_name)
        except ValueError:
            raise NameError, arg_name

        def wrapper(*args, **kwargs):
            if len(args) > arg_index:
                arg = args[arg_index]
                if not isinstance(arg, allowed_types):
                    type_list = ' or '.join(str(allowed_type) for allowed_type in allowed_types)
                    raise TypeError, "Expected '%s' to be %s; was %s." % (arg_name, type_list, type(arg))
            else:
                if arg_name in kwargs:
                    arg = kwargs[arg_name]
                    if not isinstance(arg, allowed_types):
                        type_list = ' or '.join(str(allowed_type) for allowed_type in allowed_types)
                        raise TypeError, "Expected '%s' to be %s; was %s." % (arg_name, type_list, type(arg))
            return func(*args, **kwargs)
        wrapper.wrapped_args = wrapped_args
        return wrapper
    return make_wrapper


@require('x', int, float)
@require('y', float)
def foo(x, y):
    print locals()
    return x + y


# print foo(1, 200.0)
# {'y': 200.0, 'x': 1}
# 201.0

# print foo(1.5, 2.2)
# {'y': 2.2, 'x': 1.5}
# 3.7

# print foo('asd', 2.1)
# TypeError: Expected 'x' to be <type 'int'> or <type 'float'>; was <type 'str'>.


##############################


# @require(x=(int,float), y=float)
# def foo(x,y): pass
# 
# def require(**typemap):
#     for arg_name, allowed_types in typemap:
#         if type(allowed_types) == types.TypeType:
#             allowed_types = (allowed_types,)
#         # ... proceed as before


###########################


# def types(**params):
#     def check_types(func, params=params):
#         def modified(*args, **kwargs):
#             arg_names = func.func_code.co_varnames
#             kwargs.update(zip(arg_names, args))
#             for name, _type in params.iteritems():
#                 param = kwargs[name]
#                 assert param is None or isinstance(param, _type), "Parameter '%s' should be type '%s'" % (name, _type.__name__)
#         return modified
#     return check_types
# 
# @types(foo=str, bar=bool)
# def update(foo, bar):
#     return foo
# 
# if __name__ == '__main__':
#     print update('asd', True)
# update(123, 542)
