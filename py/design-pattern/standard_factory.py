# coding:utf8
# http://dongweiming.github.io/python-abstract-factory.html


# 抽象工厂模式


from abc import ABCMeta


class StandardFactory(object):
    
    @staticmethod
    def get_factory(factory):
        ''' 根据参数找到对实际操作的工厂 '''
        if factory == 'cat':
            return CatFactory()
        elif factory == 'dog':
            return DogFactory()
        raise TypeError('unknown factory')

        raise TypeError('unknown factory')


class DogFactory(object):
    
    def get_pet(self):
        return Dog()


class CatFactory(object):
    # 和上面的方法一样，但是返回的类不同
    def get_pet(self):
        return Cat()


# 可以认为dog 和cat 都是动物的一种，可以有个基类 
class Pet(object):
    # ABCMeta 会让这个类在注册后添加很多基础抽象基类
    __metaclass__ = ABCMeta
    def eat(self):
        pass


class Dog(Pet):
    def eat(self):
        return 'dog eating..'


class Cat(Pet):
    def eat(self):
        return 'cat eating'


if __name__ == '__main__':
    factory = StandardFactory.get_factory('cat')
    pet = factory.get_pet()
    print pet.eat()
    
    factory = StandardFactory.get_factory('dog')
    pet = factory.get_pet()
    print pet.eat()
