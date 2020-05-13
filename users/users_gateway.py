import hashlib
from os import urandom
from db_schema import Database
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserGateway:
    def __init__(self):
        pass

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
        fetched = self.email_exists(email)
        if fetched is None:
            raise ValueError('No account with such email!')

        salted_password = password + fetched['salt']
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        if hashed_password == fetched['password']:
            return fetched
        else:
            return None

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
