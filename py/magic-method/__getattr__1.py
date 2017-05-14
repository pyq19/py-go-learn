# implementing __getattr__ overrides Python's default mechanism for member access.

# the __getattr__ magic method only gets invoked for attributes that are
# not in the __dict__ magic attribute.
# Implementing __getattr__ causes the hasattr buil-in function to 
# always return True, unless an exception is raised from within __getattr__

class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456

t = Test()
print 'Object variables -> %r' % t.__dict__.keys()
print t.a
print t.b
print t.c
print getattr(t, 'd')
print hasattr(t, 'x')

# Object variables -> ['a', 'b']
# a
# b
# 123456
# 123456
# True
