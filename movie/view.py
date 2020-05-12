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

    def delete_movie(self):
        movie_id = input('Enter movie id: ')

        movie = self.controller.delete_movie(movie_id)
        if movie is not None:
            print(f'Deleted successfully: [{movie.id}] - {movie.title} ({movie.rating})')
        else:
            print(f'No movie with id = {movie_id} was found')
