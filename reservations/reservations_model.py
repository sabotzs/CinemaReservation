from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from users import Users
from projections import Projections


Base = declarative_base()


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(Users.id, ondelete="cascade"))
    projection_id = Column(Integer, ForeignKey(Projections.id, ondelete="cascade"))
    row = Column(Integer, CheckConstraint("0 < row and row < 11"), nullable=False)
    col = Column(Integer, CheckConstraint("0 < col and col < 11"), nullable=False)
    user = relationship(Users, backref="reservations")
    projection = relationship(Projections, backref="reservations")


def create_reservations():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
