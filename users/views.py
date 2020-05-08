from .controllers import UserController
import sys


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        email = input('Email: ')
        password = input('Password: ')

        user = self.controller.login(email=email, password=password)
        return user

    def signin(self):
        email = input('Email: ')
        password = input('Password: ')

        user = self.controller.create_user(email=email, password=password)
        self.controller.make_client(email)
        return user

    def show_movies(self):
        movies = self.controller.show_movies()
        for movie in movies:
            print(f"[{movie['id']}] - {movie['name']} - ({movie['rating']})")

    def show_projections(self):
        movie_id = int(input('Select movie id: '))
        projections = self.controller.show_projections(movie_id)
        if projections is False:
            print('No projections for that movie!')
            return False
        else:
            self.print_projections(projections)
            return True

    def print_projections(self, projections):
        print(f"Projections for movie {projections[0]['name']}:")
        for proj in projections:
            print(f"[{proj['id']}] - {proj['day']} {proj['hour']} ({proj['movie_type']}), {100 - proj['reserv_count']}")

    def make_reservation(self, user_id):
        seats = self.get_input('Step 1 (User) Choose number of tickets: ')

        self.show_movies()
        movie_id = self.get_input('Step 2 (Movie) Choose movie by id: ')

        projections = self.controller.show_projections(movie_id)
        if projections is False:
            return

        self.print_projections(projections)
        projection_id = self.get_input('Step 3 (Projection) Choose projection by id: ')
        taken_seats = self.show_seats(seats, projection_id)
        # if there are enough seats for the projection
        if taken_seats is not None:
            selected_seats = self.select_seats(seats, taken_seats)
            self.show_projection_info(projection_id)
            seats_info = 'Seats: '
            for seat in selected_seats:
                seats_info = seats_info + str((seat)) + ' '

        confirmation = input("Step 5 (Confirm - type 'finalize'): ")
        if confirmation == 'finalize':
            self.finalize(user_id, projection_id, selected_seats)

    def get_input(self, msg):
        info = input(msg)
        if info == 'cancel':
            sys.exit()
        return int(info)

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.controller.show_seats(number_seats, projection_id)
        if taken_seats is None:
            print('Not enough available seats!')
        else:
            print('  ' + ' '.join(str(i) for i in range(1, 11)))
            for i in range(1, 11):
                row = f'{i} '
                for j in range(1, 11):
                    if (i, j) in taken_seats:
                        row = row + 'X '
                    else:
                        row = row + '. '
                print(row)
        return taken_seats

    def select_seats(self, seats, taken_seats):
        selected_seats = []
        for i in range(seats):
            done = False
            while not done:
                print(f'Step 4 (Seats): Choose seat {i + 1}:')
                row = self.get_input(f'Choose row: ')
                col = self.get_input(f'Choose column: ')

                if (row, col) in taken_seats:
                    print('This seat is already taken!')
                elif row not in range(1, 11) or col not in range(1, 11):
                    print('LOL... NO!')
                else:
                    done = True
                    taken_seats.append((row, col))
                    selected_seats.append((row, col))
        return selected_seats

    def show_projection_info(self, projection_id):
        pr_info = self.controller.show_projection_info(projection_id)
        info = f"Movie: {pr_info['name']} ({pr_info['rating']})\n" +\
            f"Date and Time: {pr_info['day']} {pr_info['hour']} ({pr_info['movie_type']})"
        print(info)

    def show_user_reservations(self, user_id):
        user_reservations = self.controller.show_user_reservations(user_id)
        for r in user_reservations:
            print(f"ID: {r['id']}, Seat ({r['row']}, {r['col']}) for {r['name']} ({r['movie_type']}) on {r['day']} at {r['hour']} ")

    def cancel_reservations(self, user_id):
        self.show_user_reservations(user_id)
        ids = input("Enter reservation ids (separated by ,):\n>>>")
        reservations_id = [int(i) for i in ids.split(',')]
        self.controller.cancel_reservations(user_id, reservations_id)

    def log_super_admin(self):
        email = input('Email for admin: ')
        password = input('Password for admin: ')

        user = self.controller.create_user(email=email, password=password)
        if user is not None:
            self.controller.log_super_admin(email)

    ##########################################
    ####### MIGHT BE IN ANOTHER FILE #########
    ##########################################

    def add_movie(self):
        name_of_the_movie = input('Please, insert the title of the movie: ')
        rating = input('Please, insert IMDB rating of the movie: ')
        self.controller.add_movie(name_of_the_movie, rating)

    def delete_movie(self):
        self.show_movies()
        movie_id = input('Please, insert the id of the movie: ')
        self.controller.delete_movie(movie_id)

    def add_projection(self):
        self.show_movies()
        movie_id = input('Please, insert the id of the movie: ')
        movie_id = int(movie_id)
        print("Possible movie types  now - 2D, 3D, 4D")
        movie_type = input('Please, insert the type of the movie:')
        day = input('Choose a date: ')
        hour = input('Choose a hour: ')
        self.controller.add_projecion(movie_id, movie_type, day, hour)

    def delete_projection(self):
        all_pr = self.controller.get_all_projections()
        for pr in all_pr:
            print(pr['name'])
            print(f"ID: {pr['id']}, on {pr['day']} at {pr['hour']} ({pr['movie_type']}) Reservations: {pr['reserv_count']}")
        projection_id = input('Select projection id: ')
        self.controller.delete_projection(projection_id)

    def hire_employee(self):
        email = input('Enter employee email: ')
        password = input('Enter employee password: ')
        employee = self.controller.create_user(email=email, password=password)
        self.controller.hire_employee(employee[0].id)

    def close_cinema(self):
        permission = input("Please, input your password for validation: ")
        close = self.controller.close_cinema(permission)
        if close is None:
            sys.exit("Cinema was closed!")
        if not close:
            print("INVALID PASSWWORD! ")

    def fire_employee(self):
        email = input('Enter employee email: ')
        permission = input("Please, input your password for validation: ")
        fired = self.controller.fire_employee(
            email=email, permission=permission)
        if isinstance(fired, str):
            return fired
        if isinstance is False:
            sys.exit("Wrong password! Access is denied! ")
        else:
            print("\n User with email ", email, "was fired! \n ")

    def log_info(func):
        def wrapper(*args):
            func(*args)
            for i in args:
                user_id = args[1]
                user_id_name = f"{user_id}" + "user" + "reservation"
                projection_id = args[2]
                seats = args[3]
            with open(f'{user_id_name}.txt', 'a') as f:
                f.write(f' *** NEW RESERVATION *** \n ')
                f.write(f"ID of user: {user_id} \n")
                f.write(f"ID of projections: {projection_id} \n")
                for i in seats:
                    f.write(f"{i} seat was added \n")
        return wrapper

    @log_info
    def finalize(self, *args):
        self.controller.reserve_seats(*args)
