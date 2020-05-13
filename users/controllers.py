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

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.model.get_seats(projection_id)
        if number_seats > 100 - len(taken_seats):
            return None
        else:
            lst_tpls = []
            for i in range(len(taken_seats)):
                seat = (taken_seats[i]['row'], taken_seats[i]['col'])
                lst_tpls.append(seat)
            return lst_tpls

    def log_super_admin(self, email):
        self.users_gateway.log_super_admin(email=email)

    def hire_employee(self, employee_id):
        self.users_gateway.hire_employee(employee_id)

    def close_cinema(self, permission):
        close = self.model.close_cinema(permission)
        return close

    def fire_employee(self, *, email, permission):
        fired = self.model.fire_employee(email=email, permission=permission)
        return fired
