from .movies_gateway import MoviesGateway


class MoviesController:
    def __init__(self):
        self.movie_getaway = MoviesGateway()

    def show_movies(self):
        movies = self.movie_getaway.show_movies()
        return movies

    def add_movie(self, title, rating):
        mes = self.movie_getaway.add_movie(title=title, rating=rating)
        return mes

    def delete_movie(self, movie_id):
        return self.movie_getaway.delete_movie(movie_id=movie_id)
