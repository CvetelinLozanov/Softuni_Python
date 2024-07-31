from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    VALID_AQUARIUMS = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    VALID_DECORATIONS = {"Ornament": Ornament, "Plant": Plant}
    VALID_FISH = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUMS:
            return "Invalid aquarium type."

        aquarium = self.VALID_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATIONS:
            return "Invalid decoration type."

        decoration = self.VALID_DECORATIONS[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        self.decorations_repository.remove(decoration)
        aquarium.decorations.append(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_FISH:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        fish = self.VALID_FISH[fish_type](fish_name, fish_species, price)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        fed_fishes = aquarium.feed()
        return f"Fish fed: {fed_fishes}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        decorations_price = sum(d.price for d in aquarium.decorations)
        fishes_price = sum(f.price for f in aquarium.fish)
        total_price = decorations_price + fishes_price
        return f"The value of Aquarium {aquarium.name} is {total_price:.2f}."

    def report(self):
        result = [str(a) for a in self.aquariums]
        return '\n'.join(result)

    def __find_aquarium_by_name(self, aquarium_name: str):
        return next((a for a in self.aquariums if a.name == aquarium_name), None)

