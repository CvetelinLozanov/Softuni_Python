from project.band_members.musician import Musician


class Guitarist(Musician):
    @property
    def available_skills(self):
        return ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)