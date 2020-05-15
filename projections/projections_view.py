from .projections_controller import ProjectionsController


class ProjectionsView:
    def __init__(self):
        self.proj_controller = ProjectionsController()

    def show_projections(self):
        movie_id = input('Select movie id: ')
        if movie_id == 'cancel':
            return False
        movie_id = int(movie_id)
        projections = self.proj_controller.show_projections(movie_id)
        if projections is False:
            print('No projections for that movie!')
            return False
        else:
            self.print_projections(projections)
            return True

    def print_projections(self, projections):
        for (proj, count) in projections:
            print(f"[{proj.id}] - {proj.day} {proj.hour} ({proj.movie_type}), {100 - count}")

    def add_projection(self, movie_id):
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
