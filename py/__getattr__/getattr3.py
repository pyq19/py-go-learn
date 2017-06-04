# coding:utf8
# http://www.jianshu.com/p/885d59db57fc


class UrlGenerator(object):
    def __init__(self, root_url):
        self.url = root_url

    def __getattr__(self, item):
        if item == 'get' or item == 'post':
            print self.url
        # return UrlGenerator('{}/{}'.format(self.url, item))
        # print '{}/{}'.format(self.url, item)
        raise ValueError('TTT~~')
        
# 用作实例属性的获取和拦截
class Test(object):
    def __init__(self, p):
        self.p = p

    def __getattr__(self, item):
        return 'default'
t = Test('asdad')
print t.p           # asdad
print t.not_exist   # default


# 自定义getattribute 的时候防止无限递归
# getattribute 在访问属性时候一直会被调用，自定义的getattribute 方法里面
# 同时需要返回相应的属性，通过self.__dict__ 取值会继续向下调用getattribute 造成循环调用
class AboutAttr(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            return super(AboutAttr, self).__getattribute__(item)
        except KeyError:
            return 'default'
# 通过调用绑定的super 对象来获取对应的属性，对新式类和object.__getattribute__(self, item) 一样
# 默认情况下自定义的类会从object 继承getattribute 方法
# getattribute 只需绑定相应的实例对象和要查找的属性名称


# 同时覆盖getattribute 和getattr 时，在getattribute 中需要抛出AttributeError 异常或手动调用getattr
class AboutAttr2(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            return super(AboutAttr2, self).__getattribute__(item)
        except KeyError:
            return 'default'
        except AttributeError as err:
            print str(err)

    def __getattr__(self, item):
        return 'never call...'

at = AboutAttr2('name lalalal')
print at.name
print at.not_exist
# name lalalal
# 'AboutAttr2' object has no attribute 'not_exist'
# None      # !!!

# getattr 不会被调用因为AttributeError 自行处理并未抛出，
# 也没有手动调用getattr，所以访问not_exist 结果是None 而不是never call...
