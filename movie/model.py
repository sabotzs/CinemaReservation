from .gateway import MovieGateway


class MovieModel:
    gateway = MovieGateway()

    def __init__(self, movie_id, title, rating):
        self.id = movie_id
        self.title = title
        self.rating = rating
