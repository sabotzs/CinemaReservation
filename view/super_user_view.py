from users.views import UserViews

def super_admin_welcome():
    views = UserViews()
    print('Hello! What would you like to do? ')
    options = f'''
        >>> "0" - Add new movie
        >>> "1" - Remove movie and all projections for it
        >>> "2" - Add projection for a movie
        >>> "3" - Remove projection for a movie
        >>> "4" - Fire somebody
        >>> "5" - Close the cinema
    '''
    print(options)
    command = input(options)
    options_dic = {"0": views.add_movie(),
    "1": views.delete_movie()}
    ### more will be added
    return options_dic.get(command)
