from .controllers import UserController


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
        return user

    def show_movies(self):
        movies = self.controller.show_movies()
        for movie in movies:
            print(f'[{movie[0]}] - {movie[1]} - ({movie[2]})')

    def show_projections(self, movie_id):
        projections = self.controller.show_projections(movie_id)
        if projections is False:
            print('No projections for that movie!')
            return False
        else:
            print(f'Projections for movie {projections[0][0]}:')
            for projection in projections:
                print(f'[{projection[1]}] - {projection[2]} {projection[3]} ({projection[4]}), {100 - projection[5]}')
            return True


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

    def show_projection_info(self, projection_id):
        pr_info = self.controller.show_projection_info(projection_id)
        info = f'Movie: {pr_info[0]} ({pr_info[1]})\n' +\
            f'Date and Time: {pr_info[2]} {pr_info[3]} ({pr_info[4]})'
        print(info)

    def reserve_seats(self, user_id, projection_id, seats):
        self.controller.reserve_seats(user_id, projection_id, seats)

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
        name_of_the_movie = input('Please, insert the  title of the movie: ')
        self.controller.delete_movie(name_of_the_movie)
