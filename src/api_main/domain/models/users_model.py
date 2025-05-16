from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    creditor = relationship("Creditor", back_populates="user")

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = generate_password_hash(password or "")

    @classmethod
    def get_user(cls, db, user_name: str):
        try:
            user = db.query(cls).filter_by(user_name=user_name).first()
            return user
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None

    @classmethod
    def check_password(cls, stored_password: str, password: str):
        return check_password_hash(stored_password, password)
    
    @classmethod
    def user_exists(cls, db, user_name: str):
        return db.query(cls).filter_by(user_name=user_name).first() is not None
        
