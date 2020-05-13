from db_schema import Database
from .reservations_gateway import ReservationsGateway


class ReservationsModel:
    def __init__(self):
        pass

    @staticmethod
    def reserve_seats(user_id, projection_id, seats):
        gateway = ReservationsGateway()
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
