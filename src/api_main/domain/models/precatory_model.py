from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.api_main.domain.models.base_model import BaseModel

class Precatory(BaseModel):
    __tablename__ = "precatorio"
    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey("credor.id"), nullable=False)
    numero_precatorio = Column(String, nullable=False)
    valor_nominal = Column(Float, nullable=False)
    foro = Column(String, nullable=True)
    data_publicacao = Column(Date, nullable=True)

    creditor = relationship("Creditor", back_populates="precatories")

    def __repr__(self):
        return f"Precatory(id={self.id}, credor_id={self.credor_id}, numero_precatorio={self.numero_precatorio}, valor_nominal={self.valor_nominal}, foro={self.foro}, data_publicacao={self.data_publicacao})"
