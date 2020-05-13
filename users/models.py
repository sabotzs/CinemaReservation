from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
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


class Clients(Users):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(Users.id, ondelete="cascade"))


def create_users():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
