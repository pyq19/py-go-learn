# coding:utf8
# http://www.dongwm.com/archives/深入描述符


class MyDescriptor(object):
    _value = ''
    def __get__(self, instance, klass):
        return self._value

    def __set__(self, instance, value):
        self._value = value.swapcase()


class Swap(object):
    swap = MyDescriptor()


instance = Swap()
print instance.swap
# 没有报AttributeError错误，因为对swap的属性访问被描述符类重载了

instance.swap = 'make it swap' # 使用__set__ 重新设置_value
print instance.swap
# MAKE IT SWAP

print instance.__dict__  # 没有用到__dict__:被劫持了
# {}


# staticmethod  classmethod

class MyStaticMethod(object):
    def __init__(self, method):
        self.staticmethod = method

    def __get__(self, object, type=None):
        return self.staticmethod


class MyClassMethod(object):
    def __init__(self, method):
        self.classmethod = method

    def __get__(self, object, klass=None):
        if klass is None:
            klass = type(object)

        def newfunc(*args):
            return self.classmethod(klass, *args)
        return newfunc


# class BaseField(object):
#     name = None
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         # ...
#         
#     def __get__(self, instance, owner):
#         return instance._data.get(self.name)
#         
#     def __set__(self, instance, value):
#         # ...
#         instance._data[self.name] = value


# werkzeug 中cached_property

class _Missing(object):
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'


_missing = _Missing()


class cached_property(property):
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __set__(self, obj, value):
        obj.__dict__[self.__name__] = value

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class Foo(object):
    @cached_property
    def bar(self):
        print 'Call me'
        return 50


foo = Foo()
print foo.bar
print foo.bar
# Call me
# 50
# 50
# 第二次调用bar 方法开始，其实调用的是缓存的结果


# 字段验证的描述符

class Quantity(object):
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('value must be > 0')


class Rectangle(object):
    height = Quantity('height')
    width = Quantity('width')

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width


r = Rectangle(10, 20)
print r.area
# 200

r = Rectangle(-1, 0)
# ValueError: value must be > 0


# 不指定Quantity 的name
class Quantity(object):
    __counter = 0
    def __init__(self):
        cls = self.__class__
        prefix = cls.__class__
        index = cls.__counter
        self.name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)
    # ...


class Rectangle(object):
    height = Quantity()
    width = Quantity()
    # ...


#####


import abc
class Validated(abc.ABC)
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        setattr(instance, self.name, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""


# 新加一个检查类型，新增一个继承了Validated 的，包含检查的validate 方法的类就可以了
class Quantity(Validated):
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value


class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value


# 函数实现描述符
def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')
    return property(qty_getter, qty_setter)
