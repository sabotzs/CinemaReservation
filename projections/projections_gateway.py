# from db_schema import Database
from .queries import (
    CHECH_MOVIE_EXISTS_BY_ID,
    INSERT_PROJECTION,
    CHECK_PROJECTION_EXISTS_BY_ID,
    DELETE_PROJECTION
)


class ProjectionsGateway:
    def __init__(self):
        pass

    def add_projection(self, *, movie_id, movie_type, day, hour):
        db = Database()
        db.cursor.execute(CHECH_MOVIE_EXISTS_BY_ID, (movie_id,))
        info = db.cursor.fetchall()
        if len(info) == 0:
            return "There is no movie with such id"

        if not isinstance(movie_type, str) or not isinstance(day, str) or not isinstance(hour, str):
            raise ValueError("Wrong input! ")
        movie_id = info[0][0]
        db.cursor.execute(INSERT_PROJECTION, (movie_id, movie_type, day, hour))
        db.connection.commit()
        db.connection.close()

    def delete_projection(self, *, projection_id):
        db = Database()
        db.cursor.execute(CHECK_PROJECTION_EXISTS_BY_ID, (projection_id,))
        info = db.cursor.fetchone()
        if info is None:
            return "No projection with such id!"
        db.cursor.execute(DELETE_PROJECTION, (projection_id,))
        db.connection.commit()
        db.connection.close()
