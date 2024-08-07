from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)

    # maybe w/o new line at the end
    def details(self):
        return (f"Fantasy - Title:{self.title}, Year:{self.year},"
                f" Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}")
    
    @property
    def age_restriction(self):
        return self.__age_restriction
    
    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value


