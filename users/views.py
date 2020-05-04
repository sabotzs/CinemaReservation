from .controllers import UserController


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        pass

    def signin(self):
        email = input('Email: ')
        password = input('password')

        self.controller.create_user(email=email, password=password)
