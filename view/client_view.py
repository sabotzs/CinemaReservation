from users.views import UserViews
import sys


def run_client_view(user):
    user_views = UserViews()

    while True:
        print('Hello! What would you like to do? ')
        options = f'1. show movies\n' +\
            f'2. show projections\n' +\
            f'3. make reservation\n' +\
            f'4. cancel reservation\n'
        
        command = int(input(options))

        options_dict = {
            1: user_views.show_movies,
            2: user_views.show_projections,
            3: user_views.make_reservation,
            4: user_views.cancel_reservations
            5: goodbye_command
        }

        f = options_dict.get(command)
        if command == 3 or command == 4:
            f(user.id)
        else:
            f()

def goodbye_command():
    sys.exit("Goodbye! Have a nice day!")