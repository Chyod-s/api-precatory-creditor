from datetime import datetime, timezone
from src.api_main.infraestructure.database.base import Base
from sqlalchemy import Column, String, DateTime

class BaseModel(Base):
    __abstract__ = True
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=True)