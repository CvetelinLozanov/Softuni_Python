from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INITIAL_SIZE = 3
    ALLOWED_AQUARIUM = 'FreshwaterAquarium'
    size_increase = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)
