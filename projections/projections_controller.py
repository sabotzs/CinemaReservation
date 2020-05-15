from .projections_gateway import ProjectionsGateway


class ProjectionsController:
    def __init__(self):
        self.proj_gateway = ProjectionsGateway()

    def show_projection_info(self, projection_id):
        pr_info = self.proj_gateway.get_projection_info(projection_id)
        return pr_info

    def show_projections(self, movie_id):
        projections = self.proj_gateway.show_projections(movie_id)
        if len(projections) == 0:
            return False
        else:
            return projections

    def add_projecion(self, movie_id, movie_type, day, hour):
        self.proj_gateway.add_projection(movie_id, movie_type, day, hour)

    def delete_projection(self, projection_id):
        self.proj_gateway.delete_projection(projection_id)

    def get_all_projections(self):
        all_proj = self.proj_gateway.get_all_projections()
        return all_proj

    def show_movies(self):
        movies = self.proj_gateway.show_movies()
        return movies
