from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    oxygen_decrease = 15

    @property
    def initial_oxygen(self):
        return 90
