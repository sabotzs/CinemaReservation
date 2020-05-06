import re
from db_schema import Database
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserModel:
    def __init__(self, *, user_id, email, password):
        self.id = user_id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        if not (re.search(regex, email)):
            raise ValueError("Wrong email! ")
        else:
            fetched = UserModel.email_exists(email)
            if fetched is not None:
                raise ValueError("Email already exists! ")
        # TODO: validate password

    @staticmethod
    def email_exists(email):
        db = Database()
        check_unique_email_query = '''
            SELECT id, email, password, salt
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(check_unique_email_query, (email,))
        fetched = db.cursor.fetchone()
        db.connection.commit()
        db.connection.close()
        return fetched


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

    @staticmethod
    def reserve_seats(user_id, projection_id, seats):
        db = Database()
        insert_reservation_query = '''
            INSERT INTO reservations (user_id, projection_id, row, col)
                VALUES (?, ?, ?, ?)
        '''
        for seat in seats:
            db.cursor.execute(insert_reservation_query, (user_id, projection_id, *seat))
        db.connection.commit()
        db.connection.close()

    @staticmethod
    def log_super_admin(email):
        db = Database()
        find_if_by_email_query = '''
            SELECT id
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(find_if_by_email_query, (email,))
        id_info = db.cursor.fetchone()
        id_info = int(id_info[0])
        insert_into_admins = '''
            INSERT INTO admins (admin_id, work_position)
                VALUES(?, ?)
        '''
        db.cursor.execute(insert_into_admins, (id_info, "super admin"))
        db.connection.commit()
        db.connection.close()
