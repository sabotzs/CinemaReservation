from .controllers import UserController
import sys


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
        self.controller.create_user(email=email, password=password)
        client = self.controller.make_client(email)
        return client

    def log_super_admin(self):
        email = input('Email for admin: ')
        password = input('Password for admin: ')

        user = self.controller.create_user(email=email, password=password)
        if user is not None:
            self.controller.log_super_admin(email)

    def hire_employee(self):
        email = input('Enter employee email: ')
        password = input('Enter employee password: ')
        employee = self.controller.create_user(email=email, password=password)
        self.controller.hire_employee(employee[0].id)

    def close_cinema(self):
        permission = input("Please, input your password for validation: ")
        close = self.controller.close_cinema(permission)
        if close is None:
            sys.exit("Cinema was closed!")
        if not close:
            print("INVALID PASSWWORD! ")

    def fire_employee(self):
        email = input('Enter employee email: ')
        permission = input("Please, input your password for validation: ")
        fired = self.controller.fire_employee(
            email=email, permission=permission)
        if isinstance(fired, str):
            return fired
        if isinstance is False:
            sys.exit("Wrong password! Access is denied! ")
        else:
            print("\n User with email ", email, "was fired! \n ")
