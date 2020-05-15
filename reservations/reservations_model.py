from db import Base
from users import Users
from projections import Projections
from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(Users.id, ondelete="cascade"))
    projection_id = Column(Integer, ForeignKey(Projections.id, ondelete="cascade"))
    row = Column(Integer, CheckConstraint("0 < row and row < 11"), nullable=False)
    col = Column(Integer, CheckConstraint("0 < col and col < 11"), nullable=False)
    user = relationship(Users, backref="reservations")
    projection = relationship(Projections, backref="reservations")
