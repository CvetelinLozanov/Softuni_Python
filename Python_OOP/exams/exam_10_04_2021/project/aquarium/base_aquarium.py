from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        if fish.ALLOWED_AQUARIUM == self.__class__.__name__:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        return "Water not suitable."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        counter = 0
        for f in self.fish:
            counter += 1
            f.eat()

        return counter

    def __str__(self):
        fishes = ' '.join(f.name for f in self.fish) if self.fish else 'none'
        decorations_count = len(self.decorations)
        result = f'{self.name}:\nFish: {fishes}\nDecorations: {decorations_count}\nComfort: {self.calculate_comfort()}'
        return result

