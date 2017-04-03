# python 3

class SomeBaseClass(object):
    def __init__(self):
        print('SomeBaseClass.__init__(self) called')


class UnsuperChild(SomeBaseClass):
    def __init__(self):
        print('UnsuperChild.__init__(self) called')
        SomeBaseClass.__init__(self)


class SuperChild(SomeBaseClass):
    def __init__(self):
        print('SuperChild.__init__(self) called')
        super(SuperChild, self).__init__()

UnsuperChild()
SuperChild()

print('*' * 30)

class InjectMe(SomeBaseClass):
    def __init__(self):
        print('InjectMe.__init__(self) called')
        super(InjectMe, self).__init__()

class UnsuperInjector(UnsuperChild, InjectMe): pass
class SuperInjector(SuperChild, InjectMe): pass

o = UnsuperInjector()
print('^' * 10)
o2 = SuperInjector()

# UnsuperChild.__init__(self) called
# SomeBaseClass.__init__(self) called
# SuperChild.__init__(self) called
# SomeBaseClass.__init__(self) called
# ******************************
# UnsuperChild.__init__(self) called
# SomeBaseClass.__init__(self) called
# ^^^^^^^^^^
# SuperChild.__init__(self) called
# InjectMe.__init__(self) called
# SomeBaseClass.__init__(self) called

