# coding:utf8
# http://www.jianshu.com/p/250f0d305c35


# 迭代器: 实现迭代协议的对象，即实现__iter__ 方法的对象.
# 描述器: 实现了描述符协议，即__get__, __set__ 和 __delete__ 方法的对象.

class WebFramework(object):
    def __init__(self, name='Flask'):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value

class PythonSite(object):
    webframework = WebFramework()

print PythonSite.webframework   # Flask
PythonSite.webframework = 'Django'
print PythonSite.webframework   # Django

# 同时实现了描述符协议__get__ 和__set__ ，该对象称为data descriptor(资料描述器)
# 仅实现__get__ 的则称为非描述器
# 两者区别在于相对于<实例的字典>的优先级
# 如果实例字典中有与描述器同名的属性，如果描述器是资料描述器，则优先使用
# 如果是非资料描述器，优先使用字典中的属性

webframework = WebFramework()
print webframework.__get__(webframework, WebFramework) # Flask


# 描述器与对象属性
class PythonSite(object):
    webframework = WebFramework()
    version = 0.01

    def __init__(self, site):
        self.site = site

pysite = PythonSite('ghost')
vars(PythonSite).items()
# [('__module__', 'descriptor_'),
#  ('version', 0.01),
#  ('__dict__', <attribute '__dict__' of 'PythonSite' objects>),
#  ('webframework', <descriptor_.WebFramework at 0x10fec27d0>),
#  ('__weakref__', <attribute '__weakref__' of 'PythonSite' objects>),
#  ('__doc__', None),
#  ('__init__', <function descriptor_.__init__>)]
vars(pysite)
# {'site': 'ghost'}
PythonSite.__dict__
# dict_proxy({'__dict__': <attribute '__dict__' of 'PythonSite' objects>,
#             '__doc__': None,
#             '__init__': <function descriptor_.__init__>,
#             '__module__': 'descriptor_',
#             '__weakref__': <attribute '__weakref__' of 'PythonSite' objects>,
#             'version': 0.01,
#             'webframework': <descriptor_.WebFramework at 0x10fec27d0>})

# vars 方法用于查看对象的属性，等价于对象的__dict__ 内容

print '=============='
# 类与实例的属性

# 类属性可以使用对象和类访问，多个实例对象共享一个类变量。但是只有类才能修改。

pysite1 = PythonSite('ghost')
pysite2 = PythonSite('admin')

print PythonSite.version
# 0.01
print pysite1.version
# 0.01
print pysite2.version
# 0.01
print pysite1.version is pysite2.version
# True
pysite1.version = 'pysite1'
print vars(pysite1)
# {'version': 'pysite1', 'site': 'ghost'}
print vars(pysite2)
# {'site': 'admin'}
PythonSite.version = 10000
print pysite1.version
# pysite1
print pysite2.version
# 10000


print '=============='
# 通常，类或实例通过 `.` 操作符访问属性
# 先访问对象的__dict__ ，如果没有再访问类（或父类，元类除外）
# 的__dict__ 。如果最后这个__dict__ 的对象是描述器，
# 则会调用描述器的__get__ 方法

print pysite1.site
# ghost
print pysite1.__dict__['site']
# ghost
print pysite2.version
# 10000
# print pysite2.__dict__['version']
# KeyError: 'version'
print type(pysite2).__dict__['version']
# 10000
print type(pysite1).__dict__['webframework']
# <__main__.WebFramework object at 0x101cd00d0>
print type(pysite1).__dict__['webframework'].__get__(None, PythonSite)
# Flask


print '+++++++'
# 实例方法，类方法，静态方法与描述器

# 调用描述器的时候，实际上会调用object.__getattribute__()
# 这取决于调用描述器的是对象还是类，
# 如果是对象object，则会调用type(obj).__dict__['x'].__get__(obj, type(obj))
# 如果是类 class.x 则会调用type(class).__dict__['x'].__get__(None, type(class))

class PythonSite(object):
    webframework = WebFramework()
    version = 0.01

    def __init__(self, site):
        self.site = site

    def get_site(self):
        return self.site

    @classmethod
    def get_version(cls):
        return cls.version

    @staticmethod
    def find_version():
        return PythonSite.version


# 类方法 @classmethod装饰器

# 类方法使用@classmethod 装饰器定义，
# 经过该装饰器的方法是一个描述器
# 类和实例都可以调用类方法

ps = PythonSite('ghost')
print ps.get_version
# <bound method type.get_version of <class '__main__.PythonSite'>>
print ps.get_version()
# 0.01
print PythonSite.get_version
# <bound method type.get_version of <class '__main__.PythonSite'>>
print PythonSite.get_version()
# 0.01

# get_version 是一个bound 方法。
# ps.get_version 这个调用会先查找它的__dict__ 是否有get_version 这个属性
# 如果没有，则查找它的类

print vars(ps)
# {'site': 'ghost'}
print type(ps).__dict__['get_version']
# <classmethod object at 0x101c3cc58>
print type(ps).__dict__['get_version'].__get__(ps, type(ps))
# <bound method type.get_version of <class '__main__.PythonSite'>>
print type(ps).__dict__['get_version'].__get__(ps, type(ps)) == ps.get_version
# True # !!!

# 并且vars(ps)中，__dict__并没有get_version这个属性，
# 依据描述器协议，将会调用type(ps).__dict__['get_version']描述器的__get__方法，
# 因为ps是实例，因此object.__getattribute__()会这样调用__get__(obj, type(obj))。

print PythonSite.__dict__['get_version']
# <classmethod object at 0x1094e2c58>
print PythonSite.__dict__['get_version'].__get__(None, PythonSite)
# <bound method type.get_version of <class '__main__.PythonSite'>>
print PythonSite.__dict__['get_version'].__get__(None, PythonSite) == PythonSite.get_version
# True


# 静态方法 @staticmethod
# 实例和类也可以调用静态方法
print ps.find_version
# <function find_version at 0x1021979b0>
print ps.find_version()
# 0.01
print vars(ps)
# {'site': 'ghost'}
print type(ps).__dict__['find_version']
# <staticmethod object at 0x102199cc8>
print type(ps).__dict__['find_version'].__get__(ps, type(ps))
# <function find_version at 0x108cbf9b0>
print type(ps).__dict__['find_version'].__get__(ps, type(ps)) == ps.find_version
# True
print PythonSite.find_version()
# 0.01
print PythonSite.find_version
# <function find_version at 0x108cbf9b0>
print type(ps).__dict__['find_version'].__get__(None, type(ps))
# <function find_version at 0x108cbf9b0>
print type(ps).__dict__['find_version'].__get__(None, type(ps)) == PythonSite.find_version
# True


# 实例方法
print ps.get_site
# <bound method PythonSite.get_site of <__main__.PythonSite object at 0x1089784d0>>
print ps.get_site()
# ghost
print type(ps).__dict__['get_site']
# <function get_site at 0x10896f8c0>
print type(ps).__dict__['get_site'].__get__(ps, type(ps))
# <bound method PythonSite.get_site of <__main__.PythonSite object at 0x1089784d0>>
print type(ps).__dict__['get_site'].__get__(ps, type(ps)) == ps.get_site
# True


print '-------------'
# 实例方法也是类的一个属性，但是对于类，描述器使其变成了unbound方法
print PythonSite.get_site
# <unbound method PythonSite.get_site>
# print PythonSite.get_site()
# TypeError: unbound method get_site() must be called with PythonSite instance as first argument (got nothing instead)
print PythonSite.get_site(ps)
# ghost
print PythonSite.__dict__['get_site']
# <function get_site at 0x1096c78c0>
print PythonSite.__dict__['get_site'].__get__(None, PythonSite)
# <unbound method PythonSite.get_site>
print PythonSite.__dict__['get_site'].__get__(None, PythonSite) == PythonSite.get_site
# True
print PythonSite.__dict__['get_site'].__get__(ps, PythonSite)
# <bound method PythonSite.get_site of <__main__.PythonSite object at 0x1096d04d0>>
print PythonSite.__dict__['get_site'].__get__(ps, PythonSite)()
# ghost


print '-----------------------'
# 描述器的应用
# 描述器的作用主要在方法和属性的定义上，即可以重新描述类的属性
# 最简单的应用是配合装饰器写一个类属性的缓存

class _Missing(object):
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'

_missing = _Missing()

class cached_property(object):
    def __init__(self, func, name=None, doc=None):
        # print self.__name__
        print self.__module__
        print self.__doc__
        # __main__
        # None
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        print self.__name__
        print self.__module__
        print self.__doc__
        # foo
        # __main__
        # None
        self.func = func

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
    def foo(self):
        print 'first calculate'
        result = 'this is result'
        return result

f = Foo()

print f.foo
print f.foo

# first calculate
# this is result
# this is result
