from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, joinedload

from .projections_model import Projections


class ProjectionsGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def add_projection(self, *, movie_id, movie_type, day, hour):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        projection = Projections(id=movie_id, movie_type=movie_type, day=day, hour=hour)
        session.add(projection)

        session.commit()
        session.close()

    def delete_projection(self, *, projection_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        session.query(Projections).filter(Projections.id == projection_id).delete()

        session.commit()
        session.close()

    def show_projections(self, movie_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        projections = session.query(Projections).\
            options(joinedload(Projections.movie),
                    joinedload(func.count(Projections.reservations)).label('reserv_count')).\
            filter(Projections.movie_id == movie_id).all()

        session.commit()
        session.close()

        return projections

    def get_projection_info(self, projection_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        projection = session.query(Projections).\
            options(joinedload(Projections.movie)).\
            filter(Projections.id == projection_id)

        session.commit()
        session.close()

        return projection

    def get_all_projections(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        projections = session.query(Projections).\
            options(joinedload(Projections.movie),
                    joinedload(func.count(Projections.reservations)).label('reserv_count')).all()

        session.commit()
        session.close()

        return projections

    def show_movies(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Check
        movies = session.query(Projections.movie).group_by(Projections.movie)

        session.commit()
        session.close()

        return movies
