from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from movies import Movies


Base = declarative_base()


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey(Movies.id, ondelete="cascade"))
    movie_type = Column(String(3))
    day = Column(String(15))
    hour = Column(String(10))
    movie = relationship(Movies, backref="projections")


def create_projections():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
