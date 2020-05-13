import re
from db_schema import Database
from .users_gateway import UserGateway


class UserModel:
    def __init__(self, *, user_id, email, password):
        self.id = user_id
        self.email = email
        self.password = password
        self.gateway = UserGateway()

    def validate(self, email, password):
        if not self.gateway.validate(email):
            raise ValueError("Wrong email! ")
        else:
            id_info = self.gateway.email_exists(email)
            if id_info is not None:
                raise ValueError("Email already exists! ")

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
    def get_seats(projection_id):
        db = Database()
        select_taken_seats = '''
            SELECT row, col
                FROM projections
                LEFT JOIN reservations
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
    def close_cinema(permission):
        gateway = UserGateway()
        close = gateway.close_cinema(permission)
        return close

    @staticmethod
    def fire_employee(*, email, permission):
        gateway = UserGateway()
        fired = gateway.fire_employee(email=email, permission=permission)
        return fired
