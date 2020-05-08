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
        if not self.validate_pass(password):
            raise ValueError("Password must contain at least 1 Upper Letter and 1 digit")
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

    def validate_pass(self, password):
        has_digit = any(char.isdigit() for char in password)
        has_upper_letter = bool(re.search('([A-Z])', password))
        if not has_digit or not has_upper_letter:
            return False
        return True

    def make_client(self, email):
        db = Database()
        select_client_query = '''
            SELECT id
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(select_client_query, (email,))
        user_id = db.cursor.fetchone()
        insert_client_query = '''
            INSERT INTO clients
                VALUES ( ? );
        '''
        db.cursor.execute(insert_client_query, user_id)
        db.connection.commit()
        db.connection.close()


    def login(self, *, email, password):
        # db = Database()
        fetched = self.email_exists(email)
        if fetched is None:
            raise ValueError('No account with such email!')

        salted_password = password + fetched['salt']
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        if hashed_password == fetched['password']:
            ######
            # return UserModel(user_id=fetched[0], email=email, password=hashed_password)
            return fetched
        else:
            return None

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

    def validate_email(self, email):
        if not (re.search(regex, email)):
            return False
        return True

    @staticmethod
    def email_exists(email):
        db = Database()
        check_unique_email_query = '''
            SELECT id, email, password, salt, work_position
                FROM users
                LEFT JOIN admins
                    on users.id = admins.admin_id
                WHERE email = ?;
        '''
        db.cursor.execute(check_unique_email_query, (email,))
        info_by_email = db.cursor.fetchone()
        db.connection.commit()
        db.connection.close()
        
        # if len(info_by_email) == 0:
        #     return None
        # else:
        #     return info_by_email
        #     info_by_email = info_by_email[0]
        return info_by_email

    def log_super_admin(self, *, email):
        db = Database()
        get_id = '''
            SELECT id
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(get_id, (email,))
        id_fetched = db.cursor.fetchone()
        id_info = int(id_fetched['id'])
        insert_into_admins = f'''
            INSERT INTO admins (admin_id, work_position)
                VALUES(?, ?)
        '''
        db.cursor.execute(insert_into_admins, (id_info, "Admin"))
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

    def delete_movie(self, *, movie_id):
        db = Database()
        get_movie_query = '''
            SELECT id
                FROM movies
                WHERE id = ?
        '''
        db.cursor.execute(get_movie_query, (movie_id,))
        info = db.cursor.fetchone()
        if info is None:
            return "That movies doesn't belong to the DB"

        delete_movie_query = '''
            DELETE
            FROM movies
            WHERE id = ?;
        '''
        db.cursor.execute(delete_movie_query, (movie_id,))
        
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
            INSERT INTO projections (movie_id, movie_type, day, hour)
            VALUES(?, ?, ?, ?);
        '''
        db.cursor.execute(insert_projection, (movie_id, movie_type, day, hour))
        db.connection.commit()
        db.connection.close()

    def delete_projection(self, *, projection_id):
        db = Database()
        check_projection_id_exists = '''
            SELECT id
                FROM projections
                WHERE id = ?;
        '''
        db.cursor.execute(check_projection_id_exists, (projection_id,))
        info = db.cursor.fetchone()
        if info is None:
            return "No projection with such id!"

        delete_projection_query = '''
            DELETE FROM projections
                WHERE id = ?;
        '''
        db.cursor.execute(delete_projection_query, (projection_id,))
        db.connection.commit()
        db.connection.close()

    def hire_employee(self, employee_id):
        db = Database()
        insert_employee_query = '''
            INSERT INTO admins (admin_id, work_position)
                VALUES ( ? , ? )
        '''
        db.cursor.execute(insert_employee_query, (employee_id, 'Employee'))
        db.connection.commit()
        db.connection.close()

    def close_cinema(self, permission):
        if not self.check_permsission(permission):
            return False
        db = Database()
        delete_proj__query = '''
            DELETE FROM projections
            WHERE movie_id != ?;
        '''
        delete_movie_query = '''
            DELETE FROM movies
            WHERE id != ?;
        '''
        db.cursor.execute(delete_proj__query, (-1,))
        db.cursor.execute(delete_movie_query, (-1,))
        db.connection.commit()
        db.connection.close()

    def check_permsission(self, permission):
        db = Database()
        find_admin = '''
            SELECT id, password, salt
                FROM users
                JOIN admins
                    ON admins.admin_id = users.id
                    WHERE admins.work_position = "Admin"
        '''
        db.cursor.execute(find_admin)
        fetched = db.cursor.fetchone()
        salted_password = permission + fetched['salt']
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        db.connection.commit()
        db.connection.close()
        if hashed_password == fetched['password']:
            return True
        return False

    def fire_employee(self, *, email, permission):
        db = Database()
        if not self.check_permsission(permission):
            return False
        find_user_query = '''
            SELECT *
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(find_user_query, (email,))
        fetched = db.cursor.fetchone()
        if fetched is None:
            return "No such user! "
        delete_user_query = '''
            DELETE FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(delete_user_query, (email,))
        db.connection.commit()
        db.connection.close()
