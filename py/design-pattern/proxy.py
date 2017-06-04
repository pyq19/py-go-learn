# coding:utf8
# http://dongweiming.github.io/python-proxy.html


# python 设计模式之代理模式
# 通过一个对象（如B）给一个对象（如A）提供·代理·的方式去访问
# 如一个对象不方便直接引用，代理就在这个对象和访问者之间做中介

# 例子
# 一个对象提供rgb 三种颜色值，若想获得它的rgb 三种颜色，
# 又不想让你获得蓝色属性

class Proxy(object):
    def __init__(self, subject):
        self.__subject = subject
    # 代理其实本质上是属性的委托
    def __getattr__(self, name):
        return getattr(self.__subject, name)


class RGB:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue
    def Red(self):
        return self.__red
    def Green(self):
        return self.__green
    def Blue(self):
        return self.__blue


class NoBlueProxy(Proxy):
    # 在子代理类拦截了blue 的访问，这样就不会返回被代理的类的Blue属性
    def Blue(self):
        return 0


if __name__ == '__main__':
    rgb = RGB(100, 192, 240)
    print rgb.Red()
    proxy = Proxy(rgb)
    print proxy.Green()
    noblue = NoBlueProxy(rgb)
    print noblue.Green()
    print noblue.Blue()

# 100
# 192
# 192
# 0
