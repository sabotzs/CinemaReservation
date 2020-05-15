from db import session_scope
from sqlalchemy import create_engine, func
from sqlalchemy.orm import joinedload
from .projections_model import Projections


class ProjectionsGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def add_projection(self, *, movie_id, movie_type, day, hour):
        with session_scope() as session:
            projection = Projections(id=movie_id, movie_type=movie_type, day=day, hour=hour)
            session.add(projection)

    def delete_projection(self, *, projection_id):
        with session_scope() as session:
            session.query(Projections).filter(Projections.id == projection_id).delete()

    def show_projections(self, movie_id):
        with session_scope() as session:
            projections = session.query(Projections, func.count(Projections.reservations).label('reserv_count')).\
                join(Projections.reservations, isouter=True).\
                filter(Projections.movie_id == movie_id).group_by(Projections.id).all()
            return projections

    def get_all_projections(self):
        with session_scope() as session:
            projections = session.query(Projections).\
                options(joinedload(Projections.movie),
                        joinedload(func.count(Projections.reservations)).label('reserv_count')).all()
            return projections
