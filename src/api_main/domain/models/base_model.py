from datetime import datetime, timezone
from src.api_main.infraestructure.database.base import Base
from sqlalchemy import Column, String, DateTime

class BaseModel(Base):
    __abstract__ = True
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=True)

    @classmethod
    def att_updated_at(cls, db, instance):
        instance.updated_at = datetime.now(timezone.utc)
        db.commit()