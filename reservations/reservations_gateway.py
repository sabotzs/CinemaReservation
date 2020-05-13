# from db_schema import Database


class ReservationsGateway:
    def __init__(self):
        pass

    def reserve_seats(self, user_id, projection_id, seats):
        db = Database()
        insert_reservation_query = '''
            INSERT INTO reservations (user_id, projection_id, row, col)
                VALUES (?, ?, ?, ?)
        '''
        for seat in seats:
            db.cursor.execute(insert_reservation_query, (user_id, projection_id, *seat))
        db.connection.commit()
        db.connection.close()
