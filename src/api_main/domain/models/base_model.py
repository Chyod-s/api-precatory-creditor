from .base import Base
from sqlalchemy import Column, Date, Integer, String

class BaseModel(Base):
    __abstract__ = True
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)