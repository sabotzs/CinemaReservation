from db_schema import Database
from .projections_gateway import ProjectionsGateway


class ProjectionsModel:
    def __init__(self):
        self.proj_gateway = ProjectionsGateway()

    @staticmethod
    def show_projections(movie_id):
        db = Database()
        select_projections_query = '''
            SELECT movies.name, projections.id, day, hour, movie_type, COUNT(reservations.id) AS reserv_count
                FROM projections
                LEFT JOIN reservations
                    ON projections.id = reservations.projection_id
                JOIN movies
                    ON projections.movie_id = movies.id
                WHERE movie_id = ?
                GROUP BY projections.id;
        '''
        db.cursor.execute(select_projections_query, (movie_id,))
        projections = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return projections

    @staticmethod
    def get_projection_info(projection_id):
        db = Database()
        select_taken_seats = '''
            SELECT name, rating, day, hour, movie_type
                FROM projections
                JOIN movies
                    ON movies.id = projections.movie_id
                WHERE projections.id = ?
        '''
        db.cursor.execute(select_taken_seats, (projection_id,))
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
        get_all_projections_query = '''
            SELECT name, projections.id AS id, day, hour, movie_type, COUNT(reservations.id) AS reserv_count
                FROM projections
                JOIN movies
                    ON projections.movie_id = movies.id
                LEFT JOIN reservations
                    ON projections.id = reservations.projection_id
                GROUP BY projections.id;
        '''
        db.cursor.execute(get_all_projections_query)
        all_pr = db.cursor.fetchall()
        return all_pr

    @staticmethod
    def delete_projection(projection_id):
        proj_gateway = ProjectionsGateway()
        proj_gateway.delete_projection(projection_id=projection_id)

    @staticmethod
    def show_movies():
        db = Database()
        select_movies_query = '''
            SELECT id, name, rating
                FROM movies
                ORDER BY rating;
        '''
        db.cursor.execute(select_movies_query)
        movies = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return movies
