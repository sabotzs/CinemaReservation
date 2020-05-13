from .movies_model import Movies
from .movies_gateway import MoviesGateway


class MoviesController:
    def __init__(self):
        self.movie_getaway = MoviesGateway()

    def show_movies(self):
        movies = self.movie_getaway.show_movies()
        return movies

    def add_movie(self, name_of_the_movie, rating):
        mes = self.movie_getaway.add_movie(name_of_the_movie, rating)
        return mes

    def delete_movie(self, movie_id):
        return self.movie_getaway.delete_movie(movie_id)
