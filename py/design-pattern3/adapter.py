# coding:utf8
# https://github.com/faif/python-patterns/blob/master/structural/adapter.py


class Dog(object):
    def __init__(self):
        self.name = 'Dog'

    def bark(self):
        return 'woof!'


class Cat(object):
    def __init__(self):
        self.name = 'Cat'

    def meow(self):
        return 'meow!'


class Human(object):
    def __init__(self):
        self.name = 'Human'

    def speak(self):
        return 'hello!'


class Car(object):
    def __init__(self):
        self.name = 'Car'

    def make_noise(self, octane_level):
        return 'vroom{0}'.format('!' * octane_level)


class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        ''' we set the adapted methods in the objects dict '''
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        ''' all non-adapted calls are passed to the object '''
        return getattr(self.obj, attr)

    def original_dict(self):
        ''' print original object dict '''
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__)
    print(objects[0].original_dict())
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print(f'A {obj.name} goes {obj.make_noise()}')


if __name__ == '__main__':
    main()

# {'name': 'Dog'}
# {'obj': <__main__.Dog object at 0x100786fd0>, 'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x100786fd0>>}
# {'name': 'Dog'}
# A Dog goes woof!
# A Cat goes meow!
# A Human goes hello!
# A Car goes vroom!!!
