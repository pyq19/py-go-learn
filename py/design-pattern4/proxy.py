# coding:utf8

# https://github.com/gennad/Design-Patterns-in-Python/blob/master/proxy.py


class IMath(object):
    ''' interface for proxy and real subject '''
    def add(self, x, y):
        raise NotImplementedError()

    def sub(self, x, y):
        raise NotImplementedError()

    def mul(self, x, y):
        raise NotImplementedError()

    def div(self, x, y):
        raise NotImplementedError()


class Math(IMath):
    ''' real subject '''
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


class Proxy(IMath):
    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        print('do something in proxy')
        return self.math.add(x, y)

    def sub(self, x, y):
        print('do something in proxy')
        return self.math.sub(x, y)

    def mul(self, x, y):
        print('do something in proxy')
        return self.math.mul(x, y)

    def div(self, x, y):
        print('do something in proxy')
        return self.math.div(x, y)

p = Proxy()
x, y = 1, 2

print('p.add', p.add(x, y))
