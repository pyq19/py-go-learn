# coding:utf8
# https://github.com/faif/python-patterns/blob/master/creational/prototype.py


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        ''' Clone a prototype and update inner attributes dictionary '''
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        ''' get all objects '''
        return self._objects

    def register_object(self, name, obj):
        ''' register an object '''
        self._objects[name] = obj

    def unregister_object(self, name):
        ''' unregister an object '''
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

# [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]
