from src.api_main.infraestructure.database.base import Base
from sqlalchemy import Column, String

class BaseModel(Base):
    __abstract__ = True
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)