from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def food_that_eats(self):
        pass

    @property
    @abstractmethod
    def weight_increase(self):
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def feed(self, food: Food):
        if type(food) not in self.food_that_eats:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def feed(self, food: Food):
        if type(food) not in self.food_that_eats:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'
