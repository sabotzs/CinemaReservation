from .model import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel

    def show_movies(self):
        movies = self.model.show_movies()
        return movies

    def add_movie(self, title, rating):
        movie = self.model.check_movie_exists(title=title)

        if movie is None:
            self.model.add_movie(title, rating)
        return movie
