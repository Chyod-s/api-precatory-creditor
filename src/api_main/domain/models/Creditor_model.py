from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Creditor(Base):
    __tablename__ = "credor"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf_cnpj = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    telefone = Column(String, nullable=True)

    precatories = relationship("Precatory", back_populates="creditor")
    personal_documents = relationship("PersonalDocument", back_populates="creditor")
    certificates = relationship("Certificate", back_populates="creditor")
    
    __doc__ = "Modelo de Usuário"

    id.__doc__ = "ID do usuário"
    nome.__doc__ = "Nome do usuário"
    cpf_cnpj.__doc__ = "CPF ou CNPJ do usuário"
    email.__doc__ = "Email do usuário"
    telefone.__doc__ = "Telefone do usuário"

    def __repr__(self):
        return f"Creditor(id={self.id}, nome={self.nome}, cpf_cnpj={self.cpf_cnpj}, email={self.email}, telefone={self.telefone})"
