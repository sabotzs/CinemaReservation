from users.views import UserViews

def super_admin_welcome():
    views = UserViews()
    print('Hello! What would you like to do? ')
    options = f'''
        >>> "1" - Add new movie
        >>> "2" - Remove movie and all projections for it
        >>> "3" - Add projection for a movie
        >>> "4" - Remove projection for a movie
        >>> "5" - Fire somebody
        >>> "6" - Close the cinema
        >>> "7" - Exit
    '''
    print(options)
    command = input(options)
    command = int(command)
    print(command)
    options_dic = {
        1: views.add_movie,
        2: views.delete_movie,
        3: views.add_projection,
        7: goodbay_command
    }
    ### more will be added
    f = options_dic.get(command)
    f()

def goodbay_command():
    print("Goodbay! Have a nice day! ")

