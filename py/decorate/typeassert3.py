# coding:utf8
# https://stackoverflow.com/questions/15299878/how-to-use-python-decorators-to-check-function-arguments

from functools import wraps

def argtype(**decls):
    """
    @argtype(name=str, text=str)
    def parse_rule(name, text): ...
    """

    def decorator(func):
        code = func.func_code
        fname = func.func_name
        names = code.co_varnames[:code.co_argcount]

        @wraps(func)
        def decorated(*args, **kwargs):
            for argname, argtype in decls.iteritems():
                try:
                    argval = args[names.index(argname)]
                except ValueError:
                    argval = kwargs.get(argname)
                if argval is None:
                    raise TypeError('%s(...): arg "%s" is null' % (fname, argname))
                if not isinstance(argval, argtype):
                    raise TypeError('%s(...): arg "%s": type is %s, must be %s' % (fname, argname, type(argval), argtype))
            return func(*args, **kwargs)
        return decorated
    return decorator

