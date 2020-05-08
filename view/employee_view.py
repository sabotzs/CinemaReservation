from users.views import UserViews
import sys


def run_employee_view(user):
    views = UserViews()

    while True:
        print('Hello! What would you like to do? ')
        options = f'''
            >>> "1" - Add new movie
            >>> "2" - Remove movie and all projections for it
            >>> "3" - Add projection for a movie
            >>> "4" - Remove projection for a movie
            >>> "5" - Exit
        '''
        command = input(options)
        command = int(command)
        options_dic = {
            1: views.add_movie,
            2: views.delete_movie,
            3: views.add_projection,
            4: views.delete_projection,
            5: goodbye_command
        }
        if command < 1 or command > 5:
            print("Wrong command! :(")
        else:
            f = options_dic.get(command)
            f()


def goodbye_command():
    sys.exit("Goodbye! Have a nice day!")
