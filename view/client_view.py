from users.views import UserViews
from projections.projections_view import ProjectionsView
import sys


def run_client_view(user):
    user_views = UserViews()
    proj_view = ProjectionsView()

    while True:
        print('Hello! What would you like to do? ')
        options = f'''
            >>> "1" - Show movies
            >>> "2" - Show projections
            >>> "3" - Make reservations
            >>> "4" - Cancel reservations
            >>> "5" - Exit
        '''
        command = int(input(options))
        options_dict = {
            1: user_views.show_movies,
            2: proj_view.show_projections,
            3: user_views.make_reservation,
            4: user_views.cancel_reservations,
            5: goodbye_command
        }

        f = options_dict.get(command)
        if command == 3 or command == 4:
            f(user.id)
        elif command < 1 or command > 5:
            print("Wrong command! :(")
        else:
            f = options_dict.get(command)
            f()


def goodbye_command():
    sys.exit("Goodbye! Have a nice day!")
