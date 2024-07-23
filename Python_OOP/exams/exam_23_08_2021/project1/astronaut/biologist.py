from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    oxygen_decrease = 5

    @property
    def initial_oxygen(self):
        return 70
