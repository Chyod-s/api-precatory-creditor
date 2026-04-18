from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Creditor(BaseModel):
    __tablename__ = "credor"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf_cnpj = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    telefone = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="creditor")
    precatories = relationship("Precatory", back_populates="creditor")
    personal_documents = relationship("PersonalDocument", back_populates="creditor")
    certificates = relationship("Certificate", back_populates="creditor")

    def __init__(self, nome: str, cpf_cnpj: str, email: str, telefone: str, user_id: int):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.email = email
        self.telefone = telefone
        self.user_id = user_id

    @classmethod
    def user_exists(cls, db, cpf_cnpj: str):
        return db.query(cls).filter_by(cpf_cnpj=cpf_cnpj).first() is not None

    @classmethod
    def get_by_id(cls, db, credor_id: int):
        return db.query(cls).filter_by(id=credor_id).all()
    
    @classmethod
    def get_by_credor_id(cls, db, user_id: int):
        return db.query(cls).filter_by(user_id=user_id).all()

    @classmethod
    def get_all_creditors(cls, db):
        return db.query(cls).all()
    
    def __repr__(self):
        return f"<Credor(nome={self.nome}, cpf_cnpj={self.cpf_cnpj}, email={self.email}, telefone={self.telefone}, user_id={self.user_id})>"
