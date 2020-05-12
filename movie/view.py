from .controller import MovieController


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def show_movies(self):
        movies = self.controller.show_movies()

        print('Current movies: ')
        for movie in movies:
            print(f'[{movie.id}] - {movie.name} ({movie.rating})')
