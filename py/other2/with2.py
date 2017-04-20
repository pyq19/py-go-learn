class MyContext(object):
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        print self._name, '__enter__'
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print self._name, '__exit__'
        return True

# >>> from wi2 import MyContext
# >>> with MyContext('a'), MyContext('b'):
# ...     print 'exec code....'
# ...
# a __enter__
# b __enter__
# exec code....
# b __exit__
# a __exit__
