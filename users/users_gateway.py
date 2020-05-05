import hashlib
from os import urandom
from db_schema import Database
from .models import UserModel


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, email, password):
        self.model.validate(email, password)
        salt = str(urandom(10))
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        insert_user_query = '''
            INSERT INTO users (email, password, salt)
                VALUES ( ? , ? , ? )
        '''
        self.db.cursor.execute(insert_user_query, (email, hashed_password, salt))
        self.db.connection.commit()

    def login(self, *, email, password):
        fetched = self.model.email_exists(email)
        if fetched is None:
            raise ValueError('No account with such email!')

        salted_password = password + fetched[3]
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        if hashed_password == fetched[2]:
            return UserModel(fetched[0], email, hashed_password)
        else:
            raise ValueError('Invalid password!')
