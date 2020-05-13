from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)


class Admins(Users):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(Users.id, ondelete="cascade"))
    work_position = Column(String(20), nullable=False)


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True)
    rating = Column(Float)


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey(Movies.id, ondelete="cascade"))
    movie_type = Column(String(3))
    day = Column(String(15))
    hour = Column(String(10))
    movie = relationship(Movies, backref="projection")


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(Users.id, ondelete="cascade"))
    projection_id = Column(Integer, ForeignKey(Projections.id, ondelete="cascade"))
    row = Column(Integer, CheckConstraint("0 < row and row < 11"), nullable=False)
    col = Column(Integer, CheckConstraint("0 < col and col < 11"), nullable=False)
    users = relationship(Users, backref="reservation")
    projections = relationship(Projections, backref="reservation")


class Clients(Users):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(Users.id, ondelete="cascade"))


engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
