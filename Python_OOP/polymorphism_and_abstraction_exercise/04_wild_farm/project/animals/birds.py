from project.animals.animal import Bird
from project.food import Meat, Seed, Fruit, Vegetable


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.25

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Meat, Seed, Fruit, Vegetable]

    @property
    def weight_increase(self):
        return 0.35

    @staticmethod
    def make_sound():
        return 'Cluck'
