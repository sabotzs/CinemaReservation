from .users_gateway import UserGateway
from .models import UserModel


class UserController:
    def __init__(self):
        self.users_gateway = UserGateway()
        self.model = UserModel

    def create_user(self, email, password):
        self.users_gateway.create(email=email, password=password)
        return self.login(email, password)

    def make_client(self, email):
        self.users_gateway.make_client(email)

    def login(self, email, password):
        fetched = self.users_gateway.login(email=email, password=password)
        if fetched is not None:
            user = UserModel(user_id=fetched['id'], email=email, password=fetched['password'])
            return user, fetched['work_position']
        else:
            raise ValueError('Invalid password!')

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
        self.model.reserve_seats(user_id, projection_id, seats)

    def show_user_reservations(self, user_id):
        user_reservations = self.model.show_user_reservations(user_id)
        return user_reservations

    def cancel_reservations(self, user_id, reservations):
        self.model.cancel_reservations(user_id, reservations)

    def log_super_admin(self, email):
        self.users_gateway.log_super_admin(email=email)

    def add_movie(self, name_of_the_movie, rating):
        self.model.add_movie(name_of_the_movie, rating)

    def delete_movie(self, movie_id):
        self.model.delete_movie(movie_id)

    def add_projecion(self, movie_id, movie_type, day, hour):
        self.model.add_projection(movie_id, movie_type, day, hour)

    def get_all_projections(self):
        all_proj = self.model.get_all_projections()
        return all_proj

    def delete_projection(self, projection_id):
        self.model.delete_projection(projection_id)

    def hire_employee(self, employee_id):
        self.users_gateway.hire_employee(employee_id)

    def close_cinema(self, permission):
        close = self.model.close_cinema(permission)
        return close
