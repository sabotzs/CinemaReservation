from db import session_scope
from sqlalchemy import create_engine
from .movies_model import Movies


class MoviesGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def add_movie(self, *, name_of_the_movie, rating):
        with session_scope() as session:
            movie_check = session.query(Movies).filter(Movies.name == name_of_the_movie).one_or_none()
            if movie_check is not None:
                return False
            if not self.validate_movie_info(name_of_the_movie, rating):
                return False
            movie = Movies(name=name_of_the_movie, rating=rating)
            session.add(movie)
            return True

    def validate_movie_info(self, name, rating):
        if not isinstance(name, str) or not isinstance(rating, float):
            return False
        return True

    def delete_movie(self, *, movie_id):
        with session_scope() as session:
            session.query(Movies).filter(Movies.id == movie_id).delete()
            return "Successfully deleted"

    def show_movies(self):
        with session_scope() as session:
            movies = session.query(Movies).order_by(Movies.id.desc())
            return movies
