from users.views import UserViews
from cinema_reservation.movie import MovieView
import sys


def run_admin_view(user):
    views = UserViews()
    movie_view = MovieView()

    while True:
        print('Hello! What would you like to do? ')
        options = f'''
            >>> "1" - Add new movie
            >>> "2" - Remove movie and all projections for it
            >>> "3" - Add projection for a movie
            >>> "4" - Remove projection for a movie
            >>> "5" - Hire employee
            >>> "6" - Fire employee
            >>> "7" - Close the cinema
            >>> "8" - Exit
        '''
        command = input(options)
        command = int(command)
        options_dic = {
            1: movie_view.add_movie,
            2: movie_view.delete_movie,
            3: views.add_projection,
            4: views.delete_projection,
            5: views.hire_employee,
            6: views.fire_employee,
            7: views.close_cinema,
            8: goodbye_command
        }
        if command < 1 or command > 8:
            print("Wrong command! :(")
        else:
            f = options_dic.get(command)
            f()


def goodbye_command():
    sys.exit("Goodbye! Have a nice day!")


def create_super_admin():
    user_views = UserViews()
    user_views.log_super_admin()
