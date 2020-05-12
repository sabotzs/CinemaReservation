from .model import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel

    def show_movies(self):
        movies = self.model.show_movies()
        return movies
