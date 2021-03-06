# from users.views import UserViews
from projections.projections_view import ProjectionsView
from reservations.reservations_view import ReservationsView
from movies.movies_view import MoviesView
import sys


def run_client_view(user):
    # user_views = UserViews()
    proj_view = ProjectionsView()
    movies_view = MoviesView()
    res_view = ReservationsView()

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
            1: movies_view.show_movies,
            2: proj_view.show_projections,
            3: make_reservation,
            4: res_view.cancel_reservations,
            5: goodbye_command
        }

        f = options_dict.get(command)
        if command == 3 or command == 4:
            f(user.user_id)
        elif command < 1 or command > 5:
            print("Wrong command! :(")
        else:
            f = options_dict.get(command)
            f()


def make_reservation(user_id):
    proj_view = ProjectionsView()
    movies_view = MoviesView()
    res_view = ReservationsView()

    movies_view.show_movies()
    projections = proj_view.show_projections()
    if projections is False:
        return
    res_view.make_reservation(user_id)


def goodbye_command():
    sys.exit("Goodbye! Have a nice day!")
