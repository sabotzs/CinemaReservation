import hashlib
import re
from os import urandom
from db import session_scope
from sqlalchemy import create_engine
from .models import Users, Clients, Admins
from movies import Movies
from projections import Projections

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def create(self, *, email, password):
        if not self.validate_pass(password):
            raise ValueError("Password must contain at least 1 Upper Letter and 1 digit")
        if not self.validate_email(email) or self.email_exists(email) is not None:
            raise ValueError("That user already exists!")

        salt = str(urandom(10))
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        with session_scope() as session:
            user = Users(email=email, password=hashed_password, salt=salt)
            session.add(user)

    def validate_pass(self, password):
        has_digit = any(char.isdigit() for char in password)
        has_upper_letter = bool(re.search('([A-Z])', password))
        if not has_digit or not has_upper_letter:
            return False
        return True

    def make_client(self, email):
        with session_scope() as session:
            user = session.query(Users).filter(Users.email == email).one()
            user_id = user.id
            client = Clients(user_id=user_id)
            session.add(client)
            return client

    def login(self, *, email, password):
        user = self.email_exists(email)
        if user is None:
            raise ValueError('No account with such email!')

        salted_password = password + user.salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        if hashed_password == user.password:
            return self.check_status(user.id)
        else:
            return None

    def validate_email(self, email):
        if not (re.search(regex, email)):
            return False
        return True

    def check_status(self, user_id):
        with session_scope() as session:
            user = session.query(Admins).filter(Admins.user_id == user_id).one_or_none()
            if user is None:
                user = session.query(Clients).filter(Clients.user_id == user_id).one()
            return user

    def email_exists(self, email):
        with session_scope() as session:
            info_by_email = session.query(Users).filter(Users.email == email).one_or_none()
            return info_by_email

    def log_super_admin(self, *, email):
        with session_scope() as session:
            user_id = session.query(Users.id).filter(Users.email == email).one()
            admin = Admins(user_id=user_id[0], work_position="Admin")
            session.add(admin)

    def hire_employee(self, employee_id):
        with session_scope() as session:
            admin = Admins(user_id=employee_id, work_position="Employee")
            session.add(admin)

    def close_cinema(self, permission):
        if not self.check_permsission(permission):
            return False
        with session_scope() as session:
            session.query(Projections).delete()
            session.query(Movies).delete()

    def check_permsission(self, permission):
        with session_scope() as session:
            user_info = session.query(Users).join(Admins.id).filter(Admins.work_position == "Admin").one()
            salted_password = permission + user_info.salt
            hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
            if hashed_password == user_info.password:
                return True
            return False

    def fire_employee(self, *, email, permission):
        if not self.check_permsission(permission):
            return False

        with session_scope() as session:
            user_id = session.query(Users.id).filter(email == email).one_or_none()
            if user_id is None:
                return "No such user! "
            session.query(Users).filter(Users.id == user_id).delete()
