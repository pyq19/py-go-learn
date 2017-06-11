# coding:utf8
# http://python.jobbole.com/81211/


class TypedProperty(object):
    def __init__(self, name, _type, default=None):
        self.name = '_' + name
        self._type = _type
        # TypeError: type() takes 1 or 3 arguments ???
        self.default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError('must be a %s' % self._type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError('cant delete attribute')


class Foo(object):
    name = TypedProperty('name', str)
    num = TypedProperty('num', int, 42)


f = Foo()
f.name = 'asd'
f.num = 321
print(f.name)
print(f.num)

f.num = 'ERROR'
