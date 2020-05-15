from .projections_controller import ProjectionsController


class ProjectionsView:
    def __init__(self):
        self.proj_controller = ProjectionsController()

    def show_projections(self):
        movie_id = int(input('Select movie id: '))
        projections = self.proj_controller.show_projections(movie_id)
        if projections is False:
            print('No projections for that movie!')
            return False
        else:
            self.print_projections(projections)
            return True

    def print_projections(self, projections):
        for proj in projections:
            print(f"[{proj.id}] - {proj.day} {proj.hour} ({proj.movie_type}), {100 - proj.reserv_count}")

    def show_projection_info(self, projection_id):
        proj = self.proj_controller.show_projection_info(projection_id)
        info = f"Movie: {proj.movie.name} ({proj.movie.rating})\n" +\
            f"Date and Time: {proj.day} {proj.hour} ({proj.movie_type})"
        print(info)

    def add_projection(self):
        self.show_movies()
        movie_id = input('Please, insert the id of the movie: ')
        movie_id = int(movie_id)
        print("Possible movie types  now - 2D, 3D, 4D")
        movie_type = input('Please, insert the type of the movie:')
        day = input('Choose a date: ')
        hour = input('Choose a hour: ')
        self.proj_controller.add_projecion(movie_id, movie_type, day, hour)

    def delete_projection(self):
        projections = self.proj_controller.get_all_projections()
        self.print_projections(projections)

        projection_id = input('Select projection id: ')
        self.proj_controller.delete_projection(projection_id)

    def show_movies(self):
        movies = self.proj_controller.show_movies()
        for movie in movies:
            print(f"[{movie['id']}] - {movie['name']} - ({movie['rating']})")
