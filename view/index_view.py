from users.views import UserViews
from .admin_view import run_admin_view
from .employee_view import run_employee_view
from .client_view import run_client_view
from users import Clients, Admins


def login():
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()

    if command == 1:
        user = user_views.login()
    elif command == 2:
        user = user_views.signin()
    else:
        raise ValueError(f'Unknown command {command}.')

    if isinstance(user, Client):
        run_client_view(user[0])
    elif user.work_possition == "Admin":
        run_admin_view(user[0])
    elif user.work_possition == "Employee":
        run_employee_view(user[0])
