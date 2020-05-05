from .controllers import UserController


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        email = input('Email: ')
        password = input('Password: ')

        self.controller.login(email=email, password=password)

    def signin(self):
        email = input('Email: ')
        password = input('Password: ')

        self.controller.create_user(email=email, password=password)
