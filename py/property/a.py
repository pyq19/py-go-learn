# http://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work

class C(object):
    def __init__(self):
        self.x = None
    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    
    x = property(getx, setx, delx, "I'm the 'x' property.")

class C2(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

# @property
# def x(self):
#     return self._x
# 
# def getx(self):
#     return self._x
# x = property(getx)

class Thing:
    def __init__(self, my_word):
        self._word = my_word

    @property
    def word(self):
        return self._word
# print Thing('oko').word    OUTPUT: oko

class Thing2:
    def __init__(self, my_word):
        self._word = my_word

    def word(self):
        return self._word
#print Thing('okokokok').word()
