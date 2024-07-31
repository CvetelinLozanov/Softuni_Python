from project.aquarium.base_aquarium import BaseAquarium
from project.fish.base_fish import BaseFish


class FreshwaterAquarium(BaseAquarium):
    CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

