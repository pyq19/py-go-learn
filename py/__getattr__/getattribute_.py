#coding:utf8
# http://stackoverflow.com/questions/371753/how-is-the-getattribute-method-used

class D(object):
    def __init__(self):
        self.test = 20
        self.test2 = 21
    def __getattribute__(self, name):
        if name == 'test':
            return 0
        else:
            return object.__getattribute__(self, name)

d = D()
print d.test  # 0
print d.test2 # 21

