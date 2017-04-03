# python2

def test_metaclass(name, bases, dict):
    print 'The Class Name is', name
    print 'The Class Bases are', bases
    print 'The dict has', len(dict), 'elems, the keys are', dict.keys()
    return 'yellow'


class TestName(object, None, int, 1):
    __metaclass__ = test_metaclass
    foo = 1
    def baz(self, arr):
        pass

print 'TestName --> ', repr(TestName)


# The Class Name is TestName
# The Class Bases are (<type 'object'>, None, <type 'int'>, 1)
# The dict has 4 elems, the keys are ['baz', '__module__', 'foo', '__metaclass__']
# TestName -->  'yellow'
