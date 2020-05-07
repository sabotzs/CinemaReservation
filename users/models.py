import re
from db_schema import Database
from .users_gateway import UserGateway
# regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserModel:
    def __init__(self, *, user_id, email, password):
        self.id = user_id
        self.email = email
        self.password = password
        self.gateway = UserGateway()

    # to be class method
    def validate(self, email, password):
        if not self.gateway.validate(email):
            raise ValueError("Wrong email! ")
        else:
            id_info = self.gateway.email_exists(email)
            if id_info is not None:
                raise ValueError("Email already exists! ")
        # TODO: validate password

    # @staticmethod
    # def email_exists(email):
    #     db = Database()
    #     check_unique_email_query = '''
    #         SELECT id, email, password, salt
    #             FROM users
    #             WHERE email = ?;
    #     '''
    #     db.cursor.execute(check_unique_email_query, (email,))
    #     fetched = db.cursor.fetchone()
    #     db.connection.commit()
    #     db.connection.close()
    #     return fetched

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

    @staticmethod
    def show_projections(movie_id):
        db = Database()
        select_projections_query = '''
            SELECT movies.name, projections.id, day, hour, type, COUNT(reservations.id)
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
    def get_seats(projection_id):
        db = Database()
        select_taken_seats = '''
            SELECT row, col
                FROM projections
                JOIN reservations
                    ON projections.id = reservations.projection_id
                WHERE projections.id = ?
                ORDER BY row, col;
        '''
        db.cursor.execute(select_taken_seats, (projection_id,))
        taken_seats = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return taken_seats

    @staticmethod
    def get_projection_info(projection_id):
        db = Database()
        select_taken_seats = '''
            SELECT name, rating, day, hour, type
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

    def reserve_seats(self, user_id, projection_id, seats):
        self.gateway.reserve_seats(user_id, projection_id, seats)

    def add_movie(self, name_of_the_movie, rating):
        self.gateway.add_movie(
            name_of_the_movie=name_of_the_movie, rating=rating)

    def delete_movie(self, name_of_the_movie):
        self.gateway.delete_movie(
            name_of_the_movie=name_of_the_movie)
