from cinema_reservation.db_schema import Database
from .queries import (
    SELECT_ALL_MOVIES_QUERY,
    SELECT_MOVIE_BY_ID_QUERY,
    SELECT_MOVIE_BY_TITLE_QUERY,
    INSERT_MOVIE_QUERY
)


class MovieGateway:
    def __init__(self):
        pass

    def get_all_movies(self):
        db = Database()

        db.cursor.execute(SELECT_ALL_MOVIES_QUERY)
        movies_info = db.cursor.fetchall()

        db.connection.commit()
        db.connection.close()

        return movies_info

    def check_movie_exists(self, *, movie_id, title):
        db = Database()

        if movie_id is not None:
            db.cursor.execute(SELECT_MOVIE_BY_ID_QUERY, (movie_id,))
        elif title is not None:
            db.cursor.execute(SELECT_MOVIE_BY_TITLE_QUERY, (title,))

        movie_info = db.cursor.fetchone()

        db.connection.commit()
        db.connection.close()

        return movie_info

    def add_movie(self, title, rating):
        db = Database()

        db.cursor.execute(INSERT_MOVIE_QUERY, (title, rating))

        db.connection.commit()
        db.connection.close()
