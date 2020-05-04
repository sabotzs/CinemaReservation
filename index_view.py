def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()

    if command == 1:
        return user_views.login()
    elif command == 2:
        return user_views.signin()
    raise ValueError(f'Unknown command {command}.')