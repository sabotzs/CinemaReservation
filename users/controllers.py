from .users_gateway import UserGateway


class UserController:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, email, password):
        self.users_gateway.create(email=email, password=password)
        self.login(email, password)


    def login(self, email, password):
        user = self.users_gateway.login(email=email, password=password)
        return user

    def show_movies(self):
        movies = self.users_gateway.show_movies()
        for movie in movies:
            print(f'[{movie[0]}] - {movie[1]} - ({movie[2]})')

    def show_projections(self, movie_id):
        projections = self.users_gateway.show_projections(movie_id)
        if len(projections) == 0:
            print('No projections for that movie!')
            return False
        else:
            print(f'Projections for movie {projections[0][0]}:')
            for projection in projections:
                print(f'[{projection[1]}] - {projection[2]} {projection[3]} ({projection[4]}), {100 - projection[5]}')
            return True

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.users_gateway.get_seats(projection_id)
        if number_seats > 100 - len(taken_seats):
            print('Not enough available seats!')
            return
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

    def show_projection_info(self, projection_id):
        pr_info = self.users_gateway.get_projection_info(projection_id)
        info = f'Movie: {pr_info[0]} ({pr_info[1]})\n' +\
            f'Date and Time: {pr_info[2]} {pr_info[3]} ({pr_info[4]})'
        print(info)

    def reserve_seats(self, user_id, projection_id, seats):
        self.users_gateway.reserve_seats(user_id, projection_id, seats)

    def log_super_admin(self, email):
        self.users_gateway.log_super_admin(email=email)
