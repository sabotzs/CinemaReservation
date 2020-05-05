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
            return UserModel(user_id=fetched[0], email=email, password=hashed_password)
        else:
            raise ValueError('Invalid password!')

    def show_movies(self):
        movies = self.model.show_movies()
        return movies

    def show_projections(self, movie_id):
        projections = self.model.show_projections(movie_id)
        return projections

    def get_seats(self, projection_id):
        taken_seats = self.model.get_seats(projection_id)
        return taken_seats

    def get_projection_info(self, projection_id):
        projection_info = self.model.get_projection_info(projection_id)
        return projection_info

    def reserve_seats(self, user_id, projection_id, seats):
        self.model.reserve_seats(user_id, projection_id, seats)