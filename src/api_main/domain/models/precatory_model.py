from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Precatory(Base):
    __tablename__ = "precatory"
    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey("creditor.id"), nullable=False)
    numero_precatorio = Column(String, nullable=False)
    valor_nominal = Column(Float, nullable=False)
    foro = Column(String, nullable=True)
    data_publicacao = Column(Date, nullable=True)

    creditor = relationship("Creditor", back_populates="precatories")

    __doc__ = "Modelo de Precatório"
    id.__doc__ = "ID do precatório"
    credor_id.__doc__ = "ID do credor"
    numero_precatorio.__doc__ = "Número do precatório"
    valor_nominal.__doc__ = "Valor nominal do precatório"
    foro.__doc__ = "Fórum do precatório"
    data_publicacao.__doc__ = "Data de publicação do precatório"
    def __repr__(self):
        return f"Precatory(id={self.id}, credor_id={self.credor_id}, numero_precatorio={self.numero_precatorio}, valor_nominal={self.valor_nominal}, foro={self.foro}, data_publicacao={self.data_publicacao})"
