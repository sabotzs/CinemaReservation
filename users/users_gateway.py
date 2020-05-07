import hashlib
from os import urandom
from db_schema import Database
# from .models import UserModel
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserGateway:
    def __init__(self):
        pass
        #self.db = Database()

    def create(self, *, email, password):
        if not self.validate_email(email) or self.email_exists(email) is not None:
            raise ValueError("That user already exists!")
        db = Database()
        salt = str(urandom(10))
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        insert_user_query = '''
            INSERT INTO users (email, password, salt)
                VALUES ( ? , ? , ? )
        '''
        db.cursor.execute(insert_user_query, (email, hashed_password, salt))
        db.connection.commit()
        db.connection.close()

    def login(self, *, email, password):
        # db = Database()
        fetched = self.email_exists(email)
        if fetched is None:
            raise ValueError('No account with such email!')

        salted_password = password + fetched[3]
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        if hashed_password == fetched[2]:
            ######
            # return UserModel(user_id=fetched[0], email=email, password=hashed_password)
            return fetched
        else:
            return None


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

    def validate_email(self, email):
        if not (re.search(regex, email)):
            return False
        return True

    @staticmethod
    def email_exists(email):
        db = Database()
        check_unique_email_query = '''
            SELECT id, email, password, salt
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(check_unique_email_query, (email,))
        info_by_email = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        if len(info_by_email) == 0:
            return None
        else:
            info_by_email = info_by_email[0]
            return info_by_email

    # def log_super_admin(self, *, id_info):
    #     db = Database()
    #     insert_into_admins = f'''
    #         INSERT INTO admins (admin_id, work_position)
    #             VALUES(?, ?)
    #     '''
    #     db.cursor.execute(insert_into_admins, (id_info, "super admin"))
    #     db.connection.commit()
    #     db.connection.close()

    def log_super_admin(self, *, email):
        db = Database()
        get_id = '''
            SELECT id
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(get_id, (email,))
        id_fetched = db.cursor.fetchone()
        id_info = int(id_fetched[0])
        insert_into_admins = f'''
            INSERT INTO admins (admin_id, work_position)
                VALUES(?, ?)
        '''
        db.cursor.execute(insert_into_admins, (id_info, "super admin"))
        db.connection.commit()
        db.connection.close()

    def add_movie(self, *, name_of_the_movie, rating):
        db = Database()
        search_for_existing_movie = '''
            SELECT *
                FROM movies
                where name = ?;
        '''
        db.cursor.execute(search_for_existing_movie, (name_of_the_movie,))
        info = db.cursor.fetchone()
        if info is not None:
            return "That movie already exists! "
        insert_movie_query = '''
            INSERT INTO movies (name, rating)
                VALUES(? ,?);
        '''
        db.cursor.execute(insert_movie_query, (name_of_the_movie, rating))
        db.connection.commit()
        db.connection.close()

    def remove_movie(self, *, name_of_the_movie):
        db = Database()
        get_movie_query = '''
            SELECT id
                FROM movies
                WHERE name = ?
        '''
        db.cursor.execute(get_movie_query, (name_of_the_movie,))
        info = db.cursor.fetchone()
        if info is None:
            return "That movies doesn't belong to the DB"
        movie_id = int(info[0][0])
        delete_movie_query = '''
            DELETE
            FROM movies
            WHERE id = ?;
        '''
        db.cursor.execute(delete_movie_query, (movie_id,))
        delete_projections_query = '''
            DELETE
            FROM projections
            WHERE movie_id = ?;
        '''
        db.cursor.execute(delete_projections_query, (movie_id,))
        db.connection.commit()
        db.connection.close()
        return "Successfully deleted!"

    def add_projection(self, *, movie_id, movie_type, day, hour):
        db = Database()
        check_movie_id_exists = '''
            SELECT id
            FROM movies
            WHERE id = ?;
        '''
        db.cursor.execute(check_movie_id_exists, (movie_id,))
        info = db.cursor.fetchall()
        if len(info) == 0:
            return "There is no movie with such id"

        if not isinstance(movie_type, str) or not isinstance(day, str) or not isinstance(hour, str):
            raise ValueError("Wrong input! ")
        movie_id = info[0][0]
        insert_projection = '''
            INSERT INTO projections (movie_id, type, day, hour)
            VALUES(?, ?, ?, ?);
        '''
        db.cursor.execute(insert_projection, (movie_id, movie_type, day, hour))
        db.connection.commit()
        db.connection.close()
