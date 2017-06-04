# coding:utf8
# http://dongweiming.github.io/python-observer.html

# 观察者模式
# 当我们希望一个对象的状态发生变化，
# 那么依赖与它的所有对象都能相应变化(获得通知),
# 那么就可以用到Observer模式，
# 其中的这些依赖对象(被观察者)就是观察者的对象，
# 那个要发生变化的对象就是所谓’观察者’

# 观察者基类
class Subject(object):
    def __init__(self):
        self._observers = []

    # 添加依赖的对象
    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    # 取消添加
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    # 这里只是通知上面注册的依赖对象新的变化
    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

# 观察者类
class Data(Subject):
    def __init__(self, name=''):
        super(Data, self).__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


# 这里有两个被观察者，即依赖的对象，每次Data 有改变，这2个view 都会变动
class HexViewer(object):
    def update(self, subject):
        print 'HexViewer: Subject %s has data 0x%x' % (subject.name, subject.data)

class DecimalViewer(object):
    def update(self, subject):
        print 'DecimalViewer: Subject %s has data %d' % (subject.name, subject.data)

if __name__ == '__main__':
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view1)
    data2.attach(view2)

    print 'setting Data 1 = 10'
    data1.data = 10
    print 'setting Data 2 = 15'
    data2.data = 15
    print 'setting Data 1 = 3'
    data1.data = 3
    print 'setting Data 2 = 5'
    data2.data = 5
    print 'update data1`s view2 because view1 si be filtered'
    data1.notify(modifier=view1)
    print 'detach HexViewer from data1 and data1'
    data1.detach(view1)
    data2.detach(view2)
    print 'setting data 1 = 10'
    data1.data = 10
    print 'setting data 2 = 15'
    data2.data = 15

# setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# HexViewer: Subject Data 1 has data 0xa
# setting Data 2 = 15
# DecimalViewer: Subject Data 2 has data 15
# HexViewer: Subject Data 2 has data 0xf
# setting Data 1 = 3
# DecimalViewer: Subject Data 1 has data 3
# HexViewer: Subject Data 1 has data 0x3
# setting Data 2 = 5
# DecimalViewer: Subject Data 2 has data 5
# HexViewer: Subject Data 2 has data 0x5
# update data1`s view2 because view1 si be filtered
# HexViewer: Subject Data 1 has data 0x3
# detach HexViewer from data1 and data1
# setting data 1 = 10
# HexViewer: Subject Data 1 has data 0xa
# setting data 2 = 15
# DecimalViewer: Subject Data 2 has data 15
