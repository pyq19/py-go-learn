#coding:utf8
# implementing the `__call__` in a class causes its instances to become callables
# in other words, those instances now behave like functions.
# you can use the built-in function `callable` to test if a particular object is callable
# (`callable` returns `True` for functions, methods, and objects that have `__call__`).

class Test(object):
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
        print '-' * 30

t = Test()

t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)

# (1, 2, 3)
# {}
# ------------------------------
# ()
# {'a': 1, 'c': 3, 'b': 2}
# ------------------------------
# (4, 5, 6)
# {'e': 5, 'd': 4, 'f': 6}
# ------------------------------

# you can implement the __call__ magic method like any method of function.
# the only difference is that invoking it doesn't require a name, just the parantheses(圆括号).
