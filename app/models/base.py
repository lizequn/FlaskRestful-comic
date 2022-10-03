import datetime
from sqlalchemy import Column, DateTime
from .. import db


class BaseModel:

    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.datetime.utcnow)
    def __commit(self):
        from sqlalchemy.exc import IntegrityError
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

    def delete(self):
        db.session.delete(self)
        self.__commit()

    def save(self):
        db.session.add(self)
        self.__commit()
        return self
