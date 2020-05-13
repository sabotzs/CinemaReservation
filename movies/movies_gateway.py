from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .movies_model import Movies

from .queries import (
    SELECT_ALL_MOVIES_QUERY,
    SELECT_MOVIE_BY_TITLE_QUERY,
    INSERT_MOVIE_QUERY,
    DELETE_MOVIE_QUERY,
    SEARH_FOR_EXISTING_MOVIE
)


class MoviesGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def add_movie(self, *, name_of_the_movie, rating):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        movie_check = session.query(Movies).filter(Movies.name == name_of_the_movie).one_or_none()
        if movie_check is not None:
            return False
        if not self.validate_movie_info(name_of_the_movie, rating):
            return False
        movie = Movies(name=name_of_the_movie, rating=rating)
        session.add(movie)
        session.commit()
        session.close()
        return True

    def validate_movie_info(self, name, rating):
        if not isinstance(name, str) or not isinstance(rating, float):
            return False
        return True

    def delete_movie(self, *, movie_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(Movies).filter(Movies.id == movie_id).delete()
        session.commit()
        session.close()
        return "Successfully deleted"

    def show_movies(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        movies = session.query(Movies).order_by(Movies.id.desc())
        session.commit()
        session.close()
        return movies
