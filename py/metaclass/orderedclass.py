# here is an example of a metaclass that uses an collections.OrderDict to remember the
# order that class variables are defined.

import collections
class OrderedClass(type):
    
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result
        
class A(metaclass=OrderedClass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass


print(A.members)
# ('__module__', '__qualname__', 'one', 'two', 'three', 'four')
