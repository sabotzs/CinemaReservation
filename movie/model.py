from .gateway import MovieGateway


class MovieModel:
    gateway = MovieGateway()

    def __init__(self, movie_id, title, rating):
        self.id = movie_id
        self.title = title
        self.rating = rating

    @classmethod
    def show_movies(cls):
        movies_info = cls.gateway.get_all_movies()
        movies_list = [
            cls(movie['id'], movie['name'], movie['rating'])
            for movie in movies_info
        ]
        return movies_list