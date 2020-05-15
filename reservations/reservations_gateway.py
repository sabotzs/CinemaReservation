from db import session_scope
from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload
from .reservations_model import Reservations
from projections import Projections


class ReservationsGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def reserve_seats(self, user_id, projection_id, seats):
        reservations = [
            Reservations(user_id=user_id, projection_id=projection_id, row=seat[0], col=seat[1])
            for seat in seats
        ]
        with session_scope() as session:
            session.add_all(reservations)

    def show_user_reservations(self, user_id):
        with session_scope() as session:
            reservations = session.query().\
                options(joinedload(Reservations.projection).joinedload(Projections.movie)).\
                filter(Projections.user_id == user_id).all()
            return reservations

    def cancel_reservations(self, user_id, reservations):
        with session_scope() as session:
            user_reservations = session.query(Reservations.user_id).\
                filter(Reservations.user_id == user_id).all()

            for res in reservations:
                if (res,) in user_reservations:
                    session.query(Reservations).filter(Reservations.id == res).delete()

    def get_seats(self, projection_id):
        with session_scope() as session:
            taken_seats = session.query(Reservations.row, Reservations.col).\
                filter(Reservations.projection.id == projection_id).all()
            return taken_seats
