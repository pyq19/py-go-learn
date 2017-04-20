#coding:utf8

class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ValueError('cannot change a const attribute')
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise ValueError('cannot delete a const attribute') 
        raise AttributeError('{0} object has not attribute {1}'.format(self.__class__.__name__, name))
c = Const()
c.aaa = 'AAA'
print c.aaa # AAA
# __getattr__(self, name)        v = x.n     返回对象x 的n 属性值（如果没有直接找到）
# __getattribute(self, name)     v = x.n     返回对象x 的n 属性值
# __setattr__(self, name, value) x.n = v     将对象x 的n 属性值设置为 v
