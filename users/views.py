from .controllers import UserController


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        email = input('Email: ')
        password = input('Password: ')

        user = self.controller.login(email=email, password=password)
        return user

    def signin(self):
        email = input('Email: ')
        password = input('Password: ')

        user = self.controller.create_user(email=email, password=password)
        return user

    def show_movies(self):
        self.controller.show_movies()

    def show_projections(self, movie_id):
        projections = self.controller.show_projections(movie_id)
        return projections

    def show_seats(self, number_seats, projection_id):
        available = self.controller.show_seats(number_seats, projection_id)
        return available

    def show_projection_info(self, projection_id):
        self.controller.show_projection_info(projection_id)

    def reserve_seats(self, user_id, projection_id, seats):
        self.controller.reserve_seats(user_id, projection_id, seats)