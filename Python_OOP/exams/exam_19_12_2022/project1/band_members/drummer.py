from project.band_members.musician import Musician


class Drummer(Musician):
    @property
    def available_skills(self):
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)