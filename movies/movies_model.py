from db import Base
from sqlalchemy import Column, Integer, String, Float


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True)
    rating = Column(Float)
