from .movies_model import MoviesModel


class MoviesController:
    def __init__(self):
        self.movies_model = MoviesModel

    def show_movies(self):
        movies = self.movies_model.show_movies()
        return movies

    def add_movie(self, name_of_the_movie, rating):
        mes = self.movies_model.add_movie(name_of_the_movie, rating)
        return mes

    def delete_movie(self, movie_id):
        return self.movies_model.delete_movie(movie_id)
