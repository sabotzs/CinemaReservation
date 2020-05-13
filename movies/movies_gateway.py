# from db_schema import Database
from .queries import (
    SELECT_ALL_MOVIES_QUERY,
    SELECT_MOVIE_BY_TITLE_QUERY,
    INSERT_MOVIE_QUERY,
    DELETE_MOVIE_QUERY,
    SEARH_FOR_EXISTING_MOVIE
)


class MoviesGateway:
    def __init__(self):
        pass

    def add_movie(self, *, name_of_the_movie, rating):
        db = Database()
        db.cursor.execute(SEARH_FOR_EXISTING_MOVIE, (name_of_the_movie,))
        info = db.cursor.fetchone()
        if info is not None:
            return False
        if not self.validate_movie_info(name_of_the_movie, rating):
            return False
        db.cursor.execute(INSERT_MOVIE_QUERY, (name_of_the_movie, rating))
        db.connection.commit()
        db.connection.close()
        return True

    def validate_movie_info(self, name, rating):
        if not isinstance(name, str) or not isinstance(rating, float):
            return False
        return True

    def delete_movie(self, *, movie_id):
        db = Database()
        db.cursor.execute(DELETE_MOVIE_QUERY, (movie_id,))
        db.connection.commit()
        db.connection.close()
        return "Successfully deleted!"
