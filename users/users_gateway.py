from ..db import Database
from .models import UserModel


class UsergGateway:
    def __init__(self):
        self.model = UserModel()
        self.db = Database()

    def create(self, *, email, password):
        self.model.validate(email, password)

        self.db.cursor.execute() # TODO: create user query
