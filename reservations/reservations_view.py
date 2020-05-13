from .reservations_controller import ResercationsController
from movies import MoviesController
from projections import ProjectionsController


class ReservationsView:
    def __init__(self):
        self.res_controller = ResercationsController()
        self.proj_controller = ProjectionsController()

    def make_reservation(self, user_id):
        seats = self.get_input('Step 1 (User) Choose number of tickets: ')

        self.show_movies()
        movie_id = self.get_input('Step 2 (Movie) Choose movie by id: ')

        projections = self.proj_controller.show_projections(movie_id)
        if projections is False:
            return

        self.print_projections(projections)
        projection_id = self.get_input('Step 3 (Projection) Choose projection by id: ')
        taken_seats = self.show_seats(seats, projection_id)
        if taken_seats is not None:
            selected_seats = self.select_seats(seats, taken_seats)
            self.show_projection_info(projection_id)
            seats_info = 'Seats: '
            for seat in selected_seats:
                seats_info = seats_info + str((seat)) + ' '

        confirmation = input("Step 5 (Confirm - type 'finalize'): ")
        if confirmation == 'finalize':
            self.finalize(user_id, projection_id, selected_seats)

    def show_movies(self):
        mov_controller = MoviesController()
        movies = mov_controller.show_movies()
        for movie in movies:
            print(f"[{movie['id']}] - {movie['name']} - ({movie['rating']})")

    def print_projections(self, projections):
        print(f"Projections for movie {projections[0]['name']}:")
        for proj in projections:
            print(f"[{proj['id']}] - {proj['day']} {proj['hour']} ({proj['movie_type']}), {100 - proj['reserv_count']}")

    def show_projection_info(self, projection_id):
        pr_info = self.proj_controller.show_projection_info(projection_id)
        info = f"Movie: {pr_info['name']} ({pr_info['rating']})\n" +\
            f"Date and Time: {pr_info['day']} {pr_info['hour']} ({pr_info['movie_type']})"
        print(info)

    def get_input(self, msg):
        info = input(msg)
        if info == 'cancel':
            sys.exit()
        return int(info)

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.res_controller.show_seats(number_seats, projection_id)
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

    def show_user_reservations(self, user_id):
        user_reservations = self.res_controller.show_user_reservations(user_id)
        for r in user_reservations:
            print(f"ID: {r['id']}, Seat ({r['row']}, {r['col']}) for {r['name']} ({r['movie_type']}) on {r['day']} at {r['hour']} ")

    def cancel_reservations(self, user_id):
        self.show_user_reservations(user_id)
        ids = input("Enter reservation ids (separated by ,):\n>>>")
        reservations_id = [int(i) for i in ids.split(',')]
        self.res_controller.cancel_reservations(user_id, reservations_id)

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
        self.res_controller.reserve_seats(*args)