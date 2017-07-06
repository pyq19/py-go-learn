# coding:utf8
# python 3.6
# https://github.com/faif/python-patterns/blob/master/creational/abstract_factory.py

import random


class PetShop(object):
    ''' a pet shop '''
    def __init__(self, animal_factory=None):
        ''' pet_factory is out abstract factory. we can set it at will '''
        self.pet_factory = animal_factory

    def show_pet(self):
        ''' creates and show a pet using the abstract factory '''
        pet = self.pet_factory.get_pet()
        print(f'we have a lovely {pet}')
        print(f'it says {pet.speak()}')
        print(f'we also have {self.pet_factory.get_food()}')

# Stuff that out factory makes

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

# Factory classes

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

# Create the proper family

def get_factory():
    ''' let's be dynamic ! '''
    return random.choice([DogFactory, CatFactory])()

# Show pets with various factories

if __name__ == '__main__':
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print('=' * 30)

# we have a lovely Cat
# it says meow
# we also have cat food
# ==============================
# we have a lovely Cat
# it says meow
# we also have cat food
# ==============================
# we have a lovely Dog
# it says woof
# we also have dog food
# ==============================
