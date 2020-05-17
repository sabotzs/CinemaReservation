from db import session_scope
from .movies_model import Movies


class MoviesGateway:
    def __init__(self):
        pass

    def add_movie(self, *, title, rating):
        with session_scope() as session:
            movie_check = session.query(Movies).filter(Movies.name == title).one_or_none()
            if movie_check is not None:
                return False
            if not self.validate_movie_info(title, rating):
                return False
            movie = Movies(name=title, rating=rating)
            session.add(movie)
            return True

    def validate_movie_info(self, name, rating):
        if not isinstance(name, str) or not isinstance(rating, float):
            return False
        return True

    def delete_movie(self, *, movie_id):
        with session_scope() as session:
            deleted = session.query(Movies).filter(Movies.id == movie_id).delete()
            return deleted != 0

    def show_movies(self):
        with session_scope() as session:
            movies = session.query(Movies).order_by(Movies.rating.desc())
            return movies
