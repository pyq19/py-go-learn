# coding:utf8
# http://dongweiming.github.io/python-strategy.html


# 策略模式

# strategy 模式和抽象工厂可能最难分辨
# 抽象工厂根据提供的参数找到对应的操作工厂，
# 每个操作工厂提供了相同的接口函数，操作工厂可能是从一个基类继承的不同实现
# 例如有个鸭子基类，然后有很多品种的鸭子是不同的操作工厂
# 本来根据抽象工厂会返回这个操作工厂来获得这个特定的鸭子类型，
# 比如一个fly 的方法，但问题有些鸭子会飞，有些不会
# 实际中有Mixin 的角度

class Duck(object):
    # 明确不能直接访问基类的这个方法，它们是具体类去实现
    # kind 标识能不能飞，可以设置yes / no
    def fly(self, kind):
        raise NotImplementedError(
            'Exception raised, Duck is supposed to be an interface / abstract class!'
            )

class Duck1(Duck):
    def fly(self, kind):
        return 'Duck 1 fly kind ->', kind


class Duck2(Duck):
    def fly(self, kind):
        return 'Duck 2 fly kin ->', kind

# 这种差异化的问题派生不是最好的方法，因为不能根据某个个体的功能
# 去给基类添加这个功能，比如fly ，Duck 2 其实不需要这个方法.
# 策略模式就是分开这些易于变化的部分

class Duck(object):
    # 上面使用继承，这里通用的使用参数方式，传入的就是操作工厂的类
    def __init__(self, strategy=None):
        self.action = None
        self.count = 0
        if strategy:
            # 指定策略，那么执行action 就是用这个类的实例
            self.action = strategy()

    def fly(self, kind):
        if self.action:
            self.count += 1
            # 这里的第二个参数self, 就是为了让操作的方法获得这里计算好的count
            return self.action.fly(kind, self)
        else:
            raise UnboundLocalError(
                'Exception raised, no strategyClass supplied to Duck!')


class Duck1(object):
    
    def fly(self, kind, instance):
        return 'duck 1 fly kind ->', kind, '#', str(instance.count)


class Duck2(object):
    
    def fly(self, kind, instance):
        return 'duck 2 fly kind ->', kind, '#', str(instance.count)


if __name__ == '__main__':
    duckfly = Duck()
    duck_1_fly = Duck(strategy=Duck1)
    duck_2_fly = Duck(strategy=Duck2)

    try:
        print duckfly.fly('yes')
    except Exception as e:
        print 'the following exception was excepted: '
        print e

    print duck_1_fly.fly('yes')
    print duck_1_fly.fly('no')
    print duck_2_fly.fly('yes')
    print duck_2_fly.fly('no')
    print duck_1_fly.fly('yes')

# the following exception was excepted:
# Exception raised, no strategyClass supplied to Duck!
# ('duck 1 fly kind ->', 'yes', '#', '1')
# ('duck 1 fly kind ->', 'no', '#', '2')
# ('duck 2 fly kind ->', 'yes', '#', '1')
# ('duck 2 fly kind ->', 'no', '#', '2')
# ('duck 1 fly kind ->', 'yes', '#', '3')
