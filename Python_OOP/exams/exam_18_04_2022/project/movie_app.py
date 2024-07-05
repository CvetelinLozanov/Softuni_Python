from typing import List
from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        user = self._get_user(username)
        if user:
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self._get_user(username)
        if not user:
            raise Exception("This user does not exist!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in user.movies_owned:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        pass

    def delete_movie(self, username: str, movie: Movie):
        pass

    def like_movie(self, username: str, movie: Movie):
        pass

    def dislike_movie(self, username: str, movie: Movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass

    def _get_user(self, username):
        return next((u for u in self.users_collection if u.username == username), None)


