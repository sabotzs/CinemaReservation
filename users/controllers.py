from .users_gateway import UserGateway


class UserController:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, email, password):
        self.users_gateway.create(email=email, password=password)
        # return self.login(email, password)

    def make_client(self, email):
        return self.users_gateway.make_client(email)

    def login(self, email, password):
        user = self.users_gateway.login(email=email, password=password)
        if user is not None:
            return user
        else:
            raise ValueError('Invalid password!')

    def log_super_admin(self, email):
        self.users_gateway.log_super_admin(email=email)

    def hire_employee(self, email):
        self.users_gateway.hire_employee(email=email)

    def close_cinema(self, permission):
        close = self.users_gateway.close_cinema(permission)
        return close

    def fire_employee(self, *, email, permission):
        fired = self.users_gateway.fire_employee(email=email, permission=permission)
        return fired
