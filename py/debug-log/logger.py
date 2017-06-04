# coding:utf8
# https://stackoverflow.com/questions/862807/how-would-you-write-a-debuggable-decorator-in-python


@debuggable
def myfunc(argA, argB, argC):
    return argB + 1

DEBUG = True

def debuggable(func):
    if DEBUG:
        def decorated(*args):
            print 'Entering', func.func_name
            print ' args', args
            ret = func(*args)
            print ret
            return ret
        return decorated
    else:
        return func

@debuggable
def myfunc(this, that):
    return this + that

