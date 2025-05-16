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

    def check_password(self, senha: str):
        """ Verifica se a senha informada é a mesma do usuário """
        if not isinstance(self.password, str) or not self.password:
            return False
        return check_password_hash(self.password, senha)
    
    @classmethod
    def user_exists(cls, db, user_name):
        return db.query(cls).filter_by(user_name=user_name).first() is not None
