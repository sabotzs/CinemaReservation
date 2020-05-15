from db import Base
from movies import Movies
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey(Movies.id, ondelete="cascade"))
    movie_type = Column(String(3))
    day = Column(String(15))
    hour = Column(String(10))
    movie = relationship(Movies, backref="projections")
