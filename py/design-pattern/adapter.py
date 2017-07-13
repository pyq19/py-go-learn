# coding:utf8
# http://dongweiming.github.io/python-adapter.html


# Adapter模式

# 和抽象工厂模式不同，适应模式每个产品类的接口方法名都是一样的，比如eat.
# Adaptor 模式每个产品类的操作不尽相同


class Dog(object):
    
    def __init__(self, name):
        self.name = name

    def bark(self):
        return 'wang wang..'


def Animal(animal):
    return animal.name, animal.bark()


# 但是有很多类型的动物，其它动物不会bark
# 出现个新类Cat ，Adapter 模式也出现为了兼容Dog

class Animal(object):
    ''' 动物类的基类 '''
    # 基类不需要实现make_noise
    def make_noise(self):
        raise NotImplementedError


class Dog(Animal):
    
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        return 'wang wnag..'


# 这里为了适应，也继承了Dog 类
class CatClassAdapter(Animal, Dog):
    
    def __init__(self, name):
        Dog.__init__(self, name)

    def miaow(self):
        return 'miew miew'

    def make_noise(self):
        return self.miaow()


# 它们为了兼容都是通过make_noise 方法返回不同的相应方法
# 实际工作中存在很多不兼容的代码，它们都要继承Dog 类，
# 每新增一个动物都要写一次return self.<new_animal>()


# 继续抽象


class CatObjectAdapter(Animal):

    def __init__(self, cat):
        self.cat = cat

    def make_noise(self):
        return self.cat.miaow()

    # 属性委派，拦截属性调用
    def __getattr__(self, attr):
        return getattr(self.cat, attr)

# 这样好一点了，但是make_noise还是不灵活，它只能用来处理cat，其实想想也没必要从Animal)继承。
# 继续抽象


class AnimalAdapter(object):
    # 这次把make_noise 的规律也传入
    def __init__(self, animal, make_noise):
        self.animal = animal
        self.make_noise = make_noise

    # 继续委派属性
    def __getattr__(self, attr):
        return getattr(self.animal, attr)


####

class Dog(object):
    
    def __init__(self, name):
        self.name = name

    def bark(self):
        return 'wang wang'


class Cat(object):
    
    def __init__(self, name):
        self.name = name

    def miew(self):
        return 'miew'


class AnimalAdapter(object):
    
    def __init__(self, animal, make_noise):
        self.animal = animal
        self.make_noise = make_noise

    def __getattr__(self, attr):
        return getattr(self.animal, attr)


if __name__ == '__main__':
    fido = Dog('Fido')
    # 都是这个适应类帮助转换
    canine = AnimalAdapter(fido, fido.bark)
    whiskers = Cat('Whiskers')
    feline = AnimalAdapter(whiskers, whiskers.miew)

    for i in (canine, feline):
        print i.name, ' ->', i.make_noise()

## 抽象工厂

class CatNoise(object):
    
    def __init__(self, context):
        self.context = context

    def make_noise(self):
        return self.context.meow()

class DogNoise(object):
    
    def __init__(self, context):
        self.context = context

    def make_noise(self):
        return self.context.bark()


def noise_adapter(context):
    if isinstance(context, Cat):
        return CatNoise(context)
    elif isinstance(context, Dog):
        return DogNoise(context)
    else:
        # raise AdapterLookupError('could not find adapter')
        raise TypeError('could not find adapter')


noise_adapter_lookup = {Cat: CatNoise, Dog: DogNoise}


def noise_adapter(context):
    try:
        return noise_adapter_lookup[context.__class__](context)
    except KeyError:
        raise
    
