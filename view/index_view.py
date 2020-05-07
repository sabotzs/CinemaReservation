from users.views import UserViews


def welcome():
    print('Welcome to HackCinema!')
    command = input('What would you like to do: ')
    args = command.split(' ')
    user_views = UserViews()
    user = None

    # show movies
    # in dict 
    if args[0] == 's':
        user_views.show_movies()
    if args[0] == 'p':
        user_views.show_projections(args[1])
    if args[0] == 'm':
        make_reservation(user, user_views)
    if args[0] == 'c':
        cancel_reservation(user, user_views)
    if args[0] == 'e':
        pass
    if args[0] == 'h':
        print_help()
    if args[0] == 'l':
        login()


def make_reservation(user, user_views):
    if user is None:
        user = login()
    
    command = input('Step 1 (User): Choose number of tickets\n>>> ')
    if command == 'cancel':
        return
    seats = int(command)

    user_views.show_movies()
    command = input('Step 2 (Movie): Choose movie by id:\n>>> ')
    if command == 'cancel':
        return
    movie_id = int(command)
    any_projections = user_views.show_projections(movie_id)
    if not any_projections:
        return

    command = input('Step 3 (Projection): Choose projection by id:\n>>> ')
    if command == 'cancel':
        return
    projection_id = int(command)

    selected_seats = choose_seats(user_views, seats, projection_id)
    if selected_seats is not None:
        confirmation = input("Step 5 (Confirm - type 'finalize') >>> ")
        if confirmation == 'cancel':
            return
        elif confirmation == 'finalize':
            user_views.reserve_seats(user.id, projection_id, selected_seats)


def choose_seats(user_views, seats, projection_id):
    taken_seats = user_views.show_seats(seats, projection_id)
    if taken_seats is not None:
        selected_seats = []
        for i in range(seats):
            done = False
            while not done:
                print(f'Step 4 (Seats): Choose seat {i + 1}:')
                
                row = int(input(f'Choose row >>> '))
                if row == 'cancel':
                    return
                col = int(input(f'Choose column >>> '))
                if col == 'cancel':
                    return

                if (row, col) in taken_seats:
                    print('This seat is already taken!')
                elif row not in range(1, 11) or col not in range(1, 11):
                    print('LOL... NO!')
                else:
                    done = True
                    taken_seats.append((row, col))
                    selected_seats.append((row, col))
        
        user_views.show_projection_info(projection_id)
        seats_info = 'Seats: '
        for seat in selected_seats:
            seats_info = seats_info + str((seat)) + ' '
        return selected_seats


def login():
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()

    if command == 1:
        return user_views.login()
    elif command == 2:
        return user_views.signin()
    raise ValueError(f'Unknown command {command}.')


def cancel_reservation(user, user_views):
    if user is None:
        user = user_views.login()
    if user.email == email:
        user_views.show_user_reservations(user.id)
        user_views.cancel_reservation(user.id)


def print_help():
    help_message = f'Valid commands:\n' +\
        f'- show_movies\n' +\
        f'- show_projections <movie_id>\n' +\
        f'- make_reservation (requires login)\n' +\
        f'- cancel_reservation (requires login)\n' +\
        f'- exit'
    print(help_message)
