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

    @classmethod
    def check_movie_exists(cls, *, movie_id=None, title=None):
        movie_info = cls.gateway.check_movie_exists(movie_id, title)
        if movie_info is None:
            return None
        return cls(movie_info['id'], movie_info['name'], movie_info['rating'])

    @classmethod
    def add_movie(cls, title, rating):
        cls.gateway.add_movie(title, rating)

    @classmethod
    def delete_movie(cls, movie_id):
        cls.gateway.delete_movie(movie_id)
