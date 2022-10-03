from sqlalchemy import Column, Integer, String
from .base import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comic(Base, BaseModel):
    __tablename__ = 'comic'
    id = Column(Integer(), primary_key=True)
    comic_name = Column(String(255), unique=True)
    comic_structure = Column(String(255))
    comic_script = Column(String(255))
    group = Column(Integer())
    recomm_result = Column(String(255))
    version = Column(String(255))
