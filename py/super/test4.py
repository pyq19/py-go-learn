class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


a = A()

# Base.__init__
# A.__init__
