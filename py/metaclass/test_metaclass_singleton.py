# python 2

class MetaSingleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(MetaSingleton, cls).__call__(*args, **kw)
        return cls.instance


class Foo(object):
    __metaclass__ = MetaSingleton


a = Foo()
b = Foo()

assert a is b
