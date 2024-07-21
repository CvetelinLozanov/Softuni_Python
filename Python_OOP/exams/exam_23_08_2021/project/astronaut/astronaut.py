from abc import ABC, abstractmethod


class Astronaut(ABC):

    oxygen_decrease = 10

    def __init__(self, name: str, oxygen: int = 0):
        self.name = name
        self.oxygen: int = self.initial_oxygen
        self.backpack = []

    @property
    @abstractmethod
    def initial_oxygen(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.oxygen_decrease

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
