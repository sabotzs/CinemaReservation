from .movies_gateway import MoviesGateway
from db_schema import Database


class MoviesModel:
    def __init__(self):
        self.movie_gateway = MoviesGateway()

    @staticmethod
    def show_movies():
        db = Database()
        select_movies_query = '''
            SELECT id, name, rating
                FROM movies
                ORDER BY rating;
        '''
        db.cursor.execute(select_movies_query)
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
