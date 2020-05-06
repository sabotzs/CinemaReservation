from .users_gateway import UserGateway
from .models import UserModel


class UserController:
    def __init__(self):
        self.users_gateway = UserGateway()
        self.model = UserModel

    def create_user(self, email, password):
        self.users_gateway.create(email=email, password=password)
        self.login(email, password)

    def login(self, email, password):
        user = self.users_gateway.login(email=email, password=password)
        return user

    def show_movies(self):
        movies = self.model.show_movies()
        return movies

    def show_projections(self, movie_id):
        projections = self.model.show_projections(movie_id)
        if len(projections) == 0:
            return False
        else:
            return projections

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.model.get_seats(projection_id)
        if number_seats > 100 - len(taken_seats):
            return None
        else:
            return taken_seats

    def show_projection_info(self, projection_id):
        pr_info = self.model.get_projection_info(projection_id)
        return pr_info

    def reserve_seats(self, user_id, projection_id, seats):
        self.users_gateway.reserve_seats(user_id, projection_id, seats)

    def log_super_admin(self, email):
        self.users_gateway.log_super_admin(email=email)
