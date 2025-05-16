from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=True) 

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = generate_password_hash(password or "")

    
    @classmethod
    def user_exists(cls, db, user_name):
        return db.query(cls).filter_by(user_name=user_name).first() is not None
    
    @classmethod
    def get_id_by_name(cls, db, user_id):
        return db.query(cls).filter_by(id=user_id).first()
        
    
    @classmethod
    def get_password_by_user_name(cls, db, user_name):
        return db.query(cls).filter_by(user_name=user_name).first()
    
    @classmethod
    def check_password(cls, db, user_name, password):
        user = cls.get_password_by_user_name(db, user_name)
        if user:
            return check_password_hash(user.password, password)
        return False
