import datetime
from sqlalchemy import Column,DateTime


class BaseModel:
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.datetime.utcnow)