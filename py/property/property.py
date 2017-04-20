#coding:utf8

class User(object):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value): # 这些方法重名
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


u = User()
print 'u.name = "Mike"'
u.name = 'Mike'
print 'u.__dict__ ->', u.__dict__
print 'u.name ->', u.name
print 'del u.name'
del u.name
print 'u.__dict__ ->', u.__dict__
# u.name = "Mike"
# u.__dict__ -> {'_User__name': 'Mike'}
# u.name -> Mike
# del u.name
# u.__dict__ -> {}

for k, v in User.__dict__.items():
    print '{0:12} = {1}'.format(k, v)
# __dict__     = <attribute '__dict__' of 'User' objects>
# __module__   = __main__
# __weakref__  = <attribute '__weakref__' of 'User' objects>
# name         = <property object at 0x1067a6890>
# __doc__      = None


