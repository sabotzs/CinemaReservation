from users.views import UserViews
from projections.projections_view import ProjectionsView
from movies.movies_view import MoviesView
import sys


def run_admin_view(user):
    views = UserViews()
    proj_view = ProjectionsView()
    movies_view = MoviesView()

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
            1: movies_view.add_movie,
            2: movies_view.delete_movie,
            3: add_projection,
            4: proj_view.delete_projection,
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


def add_projection():
    movies_view = MoviesView()
    proj_view = ProjectionsView()

    movies_view.show_movies()
    movie_id = int(input('Please, insert the id of the movie: '))
    proj_view.add_projection(movie_id)


def goodbye_command():
    sys.exit("Goodbye! Have a nice day!")


def create_super_admin():
    user_views = UserViews()
    user_views.log_super_admin()
