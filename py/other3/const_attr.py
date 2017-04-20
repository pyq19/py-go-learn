#coding:utf8

# !!!

class Image:
    @property
    def width(self):
        return self.__width

    def __getattr__(self, name):
        if name == 'colors':
            return set(self.__colors)
        classname = self.__class__.__name__
        if name in frozenset({'background', 'width', 'height'}):
            return self.__dict__['_{classname}__{name}'.format(**locals())]
        raise AttributeError("'{classname}' object has no attribute '{name}'".format(**locals()))

