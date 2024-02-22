from typing import List


class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals: List[str] = []
        self.fishes: List[str] = []
        self.birds: List[str] = []

    def add_animal(self, species: str, name: str):
        if species == 'mammal':
            self.mammals.append(name)
            Zoo.__animals += 1

        elif species == 'fish':
            self.fishes.append(name)
            Zoo.__animals += 1

        elif species == 'bird':
            self.birds.append(name)
            Zoo.__animals += 1

    def get_info(self, species: str):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}\nTotal animals: {Zoo.__animals}'

        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}\nTotal animals: {Zoo.__animals}'

        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}\nTotal animals: {Zoo.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    species, animal = input().split()
    zoo.add_animal(species, animal)

species_to_print = input()
print(zoo.get_info(species_to_print))
