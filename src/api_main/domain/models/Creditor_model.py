from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Creditor(Base):
    __tablename__ = "creditor"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf_cnpj = Column(String)
    email = Column(String)
    telefone = Column(String)

    __doc__ = "Modelo de Usuário"

    id.__doc__ = "ID do usuário"
    name.__doc__ = "Nome do usuário"
    cpf_cnpj.__doc__ = "CPF ou CNPJ do usuário"
    email.__doc__ = "Email do usuário"
    telefone.__doc__ = "Telefone do usuário"

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, cpf_cnpj={self.cpf_cnpj}, email={self.email}, telefone={self.telefone})"
    