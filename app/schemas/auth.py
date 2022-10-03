from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from .base import BaseModel
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class RolesUsers(BaseModel,Base):
    __tablename__='roles_users'
    id = Column(Integer(),primary_key=True)
    user_id = Column('user_id',String(32),ForeignKey('user.id'))
    role_id = Column('role_id',Integer(),ForeignKey('role.id'))


class Role(BaseModel,Base):
    __tablename__ = 'role'
    id = Column(Integer(),primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(BaseModel,Base):
    __tablename__ = 'user'
    id = Column(String(32),primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    roles = relationship('Role', secondary='roles_users',
                            backref=backref('users',lazy='dynamic'))
