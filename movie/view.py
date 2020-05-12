from .controller import MovieController


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def show_movies(self):
        movies = self.controller.show_movies()

        print('Current movies: ')
        for movie in movies:
            print(f'[{movie.id}] - {movie.name} ({movie.rating})')

    def add_movie(self):
        title = input('Enter movie title: ')
        rating = input('Enter movie rating: ')

        movie = self.controller.add_movie(title, rating)

        if movie is None:
            print(f'Added {title} with rating {rating} successfully')
        else:
            print(f'Already exists:\n [{movie.id}] - {movie.title} ({movie.rating})')
