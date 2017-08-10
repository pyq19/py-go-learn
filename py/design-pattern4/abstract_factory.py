# coding:utf8
# https://github.com/gennad/Design-Patterns-in-Python/blob/master/abstractfactory.py

import random


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print('this is a', pet)
        print('it say', pet.speak())
        print('it eats', self.pet_factory.get_food())


# stuff that out factory makes

class Dog(object):
    def speak(self):
        return 'woof'

    def __str__(self):
        return 'Dog'


class Cat(object):
    def speak(self):
        return 'meow'

    def __str__(self):
        return 'Cat'


class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return 'dog food'


class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return 'cat food'


dog_factory = DogFactory()
cat_factory = CatFactory()


def get_factory():
    return random.choice([dog_factory, cat_factory])


shop = PetShop()
for i in range(3):
    shop.pet_factory = get_factory()
    shop.show_pet()
    print('===' * 10)
