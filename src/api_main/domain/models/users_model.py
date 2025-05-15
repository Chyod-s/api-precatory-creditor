from .base_model import BaseModel
from sqlalchemy import Column, Integer, String

class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=True, unique=True)
    password_hash = Column(Integer, nullable=True)

    __doc__ = "Modelo de Usuário"
    id.__doc__ = "ID do usuário"
    user_name.__doc__ = "Nome do usuário"
    password_hash.__doc__ = "Hash da senha do usuário"

    def __repr__(self):
        return f"User(id={self.id}, user_name={self.user_name}, password_hash={self.password_hash})"
