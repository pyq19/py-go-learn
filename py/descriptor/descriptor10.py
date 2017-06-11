# coding:utf8
# https://github.com/xuelangZF/CS_Offer/blob/master/Python/Descriptor.md


# def __getattribute__(self, key):
#     v = object.__getattribute__(self, key)
#     if hasattr(v, '__get__'):
#         return v.__get__(None, self)
#     return v


class RevealAccess(object):
    
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'retrieving ', self.name
        print 'obj ->', obj
        print 'type(obj) ->', type(obj)
        print 'objtype ->', objtype
        return self.val

    def __set__(self, obj, val):
        print 'updating', self.name
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


m = MyClass()
print m.x
# retrieving  var "x"
# obj -> <__main__.MyClass object at 0x1059e6ed0>
# type(obj) -> <class '__main__.MyClass'>
# objtype -> <class '__main__.MyClass'>
# 10

m.x = 66
# updating var "x"


######################
# 属性

# 调用 property() 是建立资料描述器的一种简洁方式，
# 从而可以在访问属性时触发相应的方法调用
# property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, 'i m the `x` property')

# 当用户接口已经被授权访问属性之后，需求发生一些变化，
# 属性需要进一步处理才能返回给用户，这时 property() 能够提供很大帮助。
# 例如，一个电子表格类提供了访问单元格的方式: Cell('b10').value。
# 之后，对这个程序的改善要求在每次访问单元格时重新计算单元格的值。
# 然而，程序员并不想影响那些客户端中直接访问属性的代码。
# 那么解决方案是将属性访问包装在一个属性资料描述器中

class Cell(object):
    # ......
    def getvalue(self, object):
        '''recalculate cell before returning value'''
        self.recalc()
        return obj._value
    value = property(getvalue)

# property的纯Python的等价实现如下，这里就是用到了描述器:

class Property(object):
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None: 
            return self         # !!!
        if self.fget is None:
            raise AttributeError, 'unreadable attribute'
        return self.fget(obj)   # !!!

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError, 'cannot setattribute'
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError, 'cannot delete attribute'
        self.fdel(obj)

    def getter(self, fget):     # !!!
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

# TODO  函数和方法
#       静态方法和类方法
