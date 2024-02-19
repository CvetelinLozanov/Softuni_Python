from project.animals.animal import Mammal
from project.food import Meat, Seed, Fruit, Vegetable


class Mouse(Mammal):
    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def weight_increase(self):
        return 0.10

    @staticmethod
    def make_sound():
        return 'Squeak'


class Dog(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.40

    @staticmethod
    def make_sound():
        return 'Woof!'


class Cat(Mammal):

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def weight_increase(self):
        return 0.30

    @staticmethod
    def make_sound():
        return 'Meow'


class Tiger(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 1

    @staticmethod
    def make_sound():
        return 'ROAR!!!'
