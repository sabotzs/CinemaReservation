from .movies_gateway import MoviesGateway
# from db_schema import Database
from .queries import SELECT_ALL_MOVIES_QUERY


class MoviesModel:
    def __init__(self):
        self.movie_gateway = MoviesGateway()

    @staticmethod
    def show_movies():
        db = Database()
        db.cursor.execute(SELECT_ALL_MOVIES_QUERY)
        movies = db.cursor.fetchall()
        db.connection.commit()
        db.connection.close()
        return movies

    @staticmethod
    def add_movie(name_of_the_movie, rating):
        movie_gateway = MoviesGateway()
        mes = movie_gateway.add_movie(name_of_the_movie=name_of_the_movie, rating=rating)
        return mes

    @staticmethod
    def delete_movie(movie_id):
        movie_gateway = MoviesGateway()
        return movie_gateway.delete_movie(movie_id=movie_id)
