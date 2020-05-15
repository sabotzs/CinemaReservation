from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from .reservations_model import Reservations
from projections import Projections


class ReservationsGateway:
    def __init__(self):
        self.engine = create_engine("sqlite:///cinema.db")

    def reserve_seats(self, user_id, projection_id, seats):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        reservations = [
            Reservations(user_id=user_id, projection_id=projection_id, row=seat[0], col=seat[1])
            for seat in seats
        ]
        session.add_all(reservations)

        session.commit()
        session.close()

    def show_user_reservations(self, user_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        reservations = session.query().\
            options(joinedload(Reservations.projection).joinedload(Projections.movie)).\
            filter(Projections.user_id == user_id).all()

        session.commit()
        session.close()

        return reservations

    def cancel_reservations(self, user_id, reservations):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        user_reservations = session.query(Reservations.user_id).\
            filter(Reservations.user_id == user_id).all()

        for res in reservations:
            if (res,) in user_reservations:
                session.query(Reservations).filter(Reservations.id == res).delete()

        session.commit()
        session.close()

    def get_seats(self, projection_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        taken_seats = session.query(Reservations.row, Reservations.col).\
            filter(Reservations.projection.id == projection_id).all()

        session.commit()
        session.close()

        return taken_seats
