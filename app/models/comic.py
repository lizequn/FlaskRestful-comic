from sqlalchemy import Column, Integer, String
from .base import BaseModel
from app import db


class Comic(db.Model, BaseModel):
    __tablename__ = 'comic'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    comic_name = Column(String(255))
    comic_structure = Column(String(255))
    comic_script = Column(String(255))
    group = Column(Integer())
    recomm_result = Column(String(255))
    version = Column(String(255))

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(comic_name=_name).first()


