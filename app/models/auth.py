from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from werkzeug.security import safe_str_cmp
from .base import BaseModel
from app import db


class RolesUsers(db.Model, BaseModel):
    __tablename__='roles_users'
    id = Column(Integer(),primary_key=True)
    user_id = Column('user_id',String(32),ForeignKey('user.id'))
    role_id = Column('role_id',Integer(),ForeignKey('role.id'))


class Role(db.Model,BaseModel):
    __tablename__ = 'role'
    id = Column(Integer(),primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(name=_name).first()


class User(db.Model, BaseModel):
    __tablename__ = 'user'
    id = Column(String(32),primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    roles = relationship('Role', secondary='roles_users',
                            backref=backref('users',lazy='dynamic'))

    @classmethod
    def find_by_username(cls, _username):
        return cls.query.filter_by(username=_username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def authenticate(cls, username, password):
        user = cls.find_by_username(username)
        if user and safe_str_cmp(user.password, password):
            return user
        return None


# class ResourceRole(db.Model, BaseModel):
#     __tablename__ = 'resource_role'
#     id = db.Column(db.Integer(), primary_key=True)
#     resource_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
#     role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
#
#
# class ResourceModel(db.Model, BaseModel):
#     __tablename__ = 'resource'
#     id = db.Column(db.Integer(), primary_key=True)
#     resource = db.Column(db.String(255),unique=True)
#     description = db.Column(db.String(255))
#     roles = db.relationship('Role', secondary='resource_role',
#                             backref=db.backref('resources', lazy='dynamic'))