from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return self.MAX_SPEED

    def train(self):
        if self.speed + self.SPEED_INCREASE > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.SPEED_INCREASE
