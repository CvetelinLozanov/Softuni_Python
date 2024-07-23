from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    @property
    def initial_oxygen(self):
        return 50
