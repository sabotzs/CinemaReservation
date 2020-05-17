from db import session_scope, Base, engine
from movies import Movies
from projections import Projections


def initialize_movies():
    with session_scope() as session:
        movie_list = [
            Movies(name='Titanic', rating=7.9),
            Movies(name='The Shining', rating=8.4),
            Movies(name='Pulp Fiction', rating=8.0)
        ]
        session.add_all(movie_list)


def initialize_projections():
    with session_scope() as session:
        projections_list = [
            Projections(movie_id=1, movie_type='3D', day='2020-05-16', hour='19:00'),
            Projections(movie_id=2, movie_type='3D', day='2020-05-17', hour='23:00'),
            Projections(movie_id=2, movie_type='3D', day='2020-05-16', hour='21:00')
        ]
        session.add_all(projections_list)


def bootstrap():
    Base.metadata.create_all(engine)
