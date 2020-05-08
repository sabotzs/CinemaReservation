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
    def reserve_seats(user_id, projection_id, seats):
        gateway = UserGateway()
        gateway.reserve_seats(user_id, projection_id, seats)

    @staticmethod
    def show_user_reservations(user_id):
        db = Database()
        select_user_reservations_query = '''
            SELECT reservations.id AS id, row, col, name, movie_type, day, hour
                FROM reservations
                JOIN projections
                    ON reservations.projection_id = projections.id
                JOIN movies
                    ON projections.movie_id = movies.id
                WHERE user_id = ?;
        '''
        db.cursor.execute(select_user_reservations_query, (user_id,))
        user_reservations = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return user_reservations

    @staticmethod
    def cancel_reservations(user_id, reservations):
        db = Database()
        select_reservation_query = '''
            SELECT user_id
                FROM reservations
                WHERE id = ?;
        '''
        delete_reservation_query = '''
            DELETE FROM reservations
                WHERE id = ?;
        '''
        for r in reservations:
            db.cursor.execute(select_reservation_query, (r, ))
            u_id = db.cursor.fetchone()
            if u_id[0] == user_id:
                db.cursor.execute(delete_reservation_query, (r, ))
            else:
                print(f"You don't have a reservation {r}")
        db.connection.commit()
        db.connection.close()

    @staticmethod
    def add_movie(name_of_the_movie, rating):
        gateway = UserGateway()
        gateway.add_movie(name_of_the_movie=name_of_the_movie, rating=rating)

    @staticmethod
    def delete_movie(movie_id):
        gateway = UserGateway()
        gateway.delete_movie(movie_id=movie_id)

    @staticmethod
    def add_projection(movie_id, movie_type, day, hour):
        gateway = UserGateway()
        gateway.add_projection(
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
        gateway = UserGateway()
        gateway.delete_projection(projection_id=projection_id)

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
