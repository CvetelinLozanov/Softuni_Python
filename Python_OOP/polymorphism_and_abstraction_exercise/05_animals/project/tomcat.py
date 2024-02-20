from project.cat import Cat


class Tomcat(Cat):
    gender = 'Male'

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Tomcat.gender)

    @staticmethod
    def make_sound():
        return 'Hiss'
