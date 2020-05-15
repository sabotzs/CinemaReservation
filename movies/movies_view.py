from .movies_controller import MoviesController


class MoviesView:
    def __init__(self):
        self.movies_controller = MoviesController()

    def show_movies(self):
        movies = self.movies_controller.show_movies()
        for movie in movies:
            print(f"[{movie.id}] - {movie.name} - ({movie.rating})")

    def add_movie(self):
        name_of_the_movie = input('Please, insert the title of the movie: ')
        rating = float(input('Please, insert IMDB rating of the movie: '))
        mes = self.movies_controller.add_movie(name_of_the_movie, rating)
        if not mes:
            print(" \n ERROR! Incorect data or movie already exists! \n ")

    def delete_movie(self):
        self.show_movies()
        movie_id = input('Please, insert the id of the movie: ')
        mes = self.movies_controller.delete_movie(movie_id)
        if not mes:
            print(" \n ERROR! No movies with such id! \n ")
