from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine


Base = declarative_base()


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True)
    rating = Column(Float)


def create_movies():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
