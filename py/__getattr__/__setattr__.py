# coding:utf8
# https://gist.github.com/sente/3174676

class Foo(object):
    def __getattribute__(self, name):
        print 'getting attribute %s' % name
        return object.__getattribute__(self, name)

    def __setattr__(self, name, val):
        print 'setting attribute %s to %s' % (name, val)
        return object.__setattr__(self, name, val)

f = Foo()
f.var = 100
# setting attribute var to 100
f.name = 'asd'
# setting attribute name to asd
bar = f.var
# getting attribute var
f.var = f.name
# getting attribute name
# setting attribute var to asd
