def make_hook(f):
    '''Decorator to turn 'foo' method into '__foo__' '''
    f.is_hook = 1
    return f


class MyType(type):
    def __new__(cls, name, bases, attrs):
        if name.startswith('None'):
            return None

        # Go over attributes and see if they should be rename.
        newattrs = {}
        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_hook', 0):
                newattrs['__%s__' % attrname] = attrvalue
            else:
                newattrs[attrname] = attrvalue

        return super(MyType, cls).__new__(cls, name, bases, newattrs)

    def __init__(self, name, bases, attrs):
        super(MyType, self).__init__(name, bases, attrs)

        # classregistry.register(self, self.interfaces)
        print 'would register class %s now.' % self

    def __add__(self, other):
        class AutoClass(self, other):
            pass
        return AutoClass

    def unregister(self):
        print 'would unregister class %s now.' % self


class MyObject:
    __metaclass__ = MyType


class NoneSample(MyObject):
    pass


# will print 'NoneType None'
print type(NoneSample), repr(NoneSample)


class Example(MyObject):
    def __init__(self, value):
        self.value = value

    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)


# will unregister the class
Example.unregister()

inst = Example(10)
# will fail with an AttributeError
# inst.unregister()

print inst + inst
class Sibling(MyObject):
    pass


ExampleSibling = Example + Sibling
# ExampleSibling is now a subclass of both Example and Sibling ( with no
# content of its own ) although it will believe its called 'AutoClass'
print ExampleSibling
print ExampleSibling.__mro__
    
# OUT:
# would register class <class '__main__.MyObject'> now.
# <type 'NoneType'> None
# would register class <class '__main__.Example'> now.
# would unregister class <class '__main__.Example'> now.
# <__main__.Example object at 0x10ce3b150>
# would register class <class '__main__.Sibling'> now.
# would register class <class '__main__.AutoClass'> now.
# <class '__main__.AutoClass'>
# (<class '__main__.AutoClass'>, <class '__main__.Example'>, <class '__main__.Sibling'>, <class '__main__.MyObject'>, <type 'object'>)
