import hashlib
from os import urandom
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import re
from .models import Users, Clients, Admins

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def create(self, *, email, password):
        if not self.validate_pass(password):
            raise ValueError("Password must contain at least 1 Upper Letter and 1 digit")
        if not self.validate_email(email) or self.email_exists(email) is not None:
            raise ValueError("That user already exists!")

        Session = sessionmaker(bind=self.engine)
        session = Session()

        salt = str(urandom(10))
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        user = Users(email=email, password=hashed_password, salt=salt)
        session.add(user)
        session.commit()
        session.close()

    def validate_pass(self, password):
        has_digit = any(char.isdigit() for char in password)
        has_upper_letter = bool(re.search('([A-Z])', password))
        if not has_digit or not has_upper_letter:
            return False
        return True

    def make_client(self, email):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(Users).filter(Users.email == email).one()
        user_id = user.id
        client = Cliens(user_id=user_id)
        session.commit()
        session.close()
        return client

    def login(self, *, email, password):
        user = self.email_exists(email)
        if user is None:
            raise ValueError('No account with such email!')

        salted_password = password + user.salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        if hashed_password == user.password:
            return user
        else:
            return None

    def validate_email(self, email):
        if not (re.search(regex, email)):
            return False
        return True

    def email_exists(self, email):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        info_by_email = session.query(Users).filter(Users.email == email).one_or_none()
        session.commit()
        session.close()
        return info_by_email

    def log_super_admin(self, *, email):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user_id = session.query(Users.id).filter(Users.email == email).one()
        admin = Admins(user_id=user_id, work_position="Admin")
        session.add(admin)
        session.commit()
        session.close()

    def hire_employee(self, employee_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        admin = Admins(user_id=employee_id, work_position="Employee")

    def close_cinema(self, permission):
        if not self.check_permsission(permission):
            return False
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(Projections).delete()
        session.query(Movies).delete()
        session.commit()
        session.close()

    def check_permsission(self, permission):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user_info = session.query(Users).join(Admins.id).filter(Admins.work_position == "Admin").one()
        salted_password = permission + user_info.salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        if hashed_password == user_info.password:
            return True
        return False

    def fire_employee(self, *, email, permission):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        if not self.check_permsission(permission):
            return False
        find_user_query = '''
            SELECT *
                FROM users
                WHERE email = ?;
        '''
        user_id = session.query(Users.id).filter(email == email).one_or_none()
        if user_id is None:
            return "No such user! "
        delete_user_query = '''
            DELETE FROM users
                WHERE email = ?;
        '''
        session.query(Users).filter(Users.id == user_id).delete()
        session.commit()
        session.close()
