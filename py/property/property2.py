print '==' * 20
class User(object):
    def get_name(self): return self.__name
    def set_name(self, value): self.__name = value
    def del_name(self): del self.__name
    name = property(get_name, set_name, del_name, 'help..')

for k, v in User.__dict__.items():
    print '{0:12} = {1}'.format(k, v)
# set_name     = <function set_name at 0x1086838c0>
# name         = <property object at 0x108684998>
# del_name     = <function del_name at 0x108692938>
# __module__   = __main__
# get_name     = <function get_name at 0x1086831b8>
# __dict__     = <attribute '__dict__' of 'User' objects>
# __weakref__  = <attribute '__weakref__' of 'User' objects>
# __doc__      = None
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

