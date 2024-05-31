from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):

    CATCH_TIME = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.CATCH_TIME)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.CATCH_TIME} seconds]"