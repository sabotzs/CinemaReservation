# from db_schema import Database
from .projections_gateway import ProjectionsGateway
from .queries import (
    SELECT_PROJECTIONS,
    SLECT_TAKEN_SEATS,
    GET_ALL_PROJECTIONS,
    SLECT_MOVIES
)


class ProjectionsModel:
    def __init__(self):
        self.proj_gateway = ProjectionsGateway()

    @staticmethod
    def show_projections(movie_id):
        db = Database()
        db.cursor.execute(SELECT_PROJECTIONS, (movie_id,))
        projections = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return projections

    @staticmethod
    def get_projection_info(projection_id):
        db = Database()
        db.cursor.execute(SLECT_TAKEN_SEATS, (projection_id,))
        projection_info = db.cursor.fetchone()
        db.connection.commit()
        db.connection.close()
        return projection_info

    @staticmethod
    def add_projection(movie_id, movie_type, day, hour):
        proj_gateway = ProjectionsGateway()
        proj_gateway.add_projection(
            movie_id=movie_id, movie_type=movie_type, day=day, hour=hour)

    @staticmethod
    def get_all_projections():
        db = Database()
        db.cursor.execute(GET_ALL_PROJECTIONS)
        all_pr = db.cursor.fetchall()
        return all_pr

    @staticmethod
    def delete_projection(projection_id):
        proj_gateway = ProjectionsGateway()
        proj_gateway.delete_projection(projection_id=projection_id)

    @staticmethod
    def show_movies():
        db = Database()
        db.cursor.execute(SLECT_MOVIES)
        movies = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return movies
