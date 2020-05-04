import hashlib
from os import urandom
from ..db import Database
from .models import UserModel


class UsergGateway:
    def __init__(self):
        self.model = UserModel()
        self.db = Database()

    def create(self, *, email, password):
        self.model.validate(email, password)
        salt = urandom(10)
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        insert_user_query = '''
            INSERT INTO users (email, password, salt)
                VALUES ( ? , ? , ? )
        '''
        self.db.cursor.execute(insert_user_query, (email, hashed_password, salt))
