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
    
    @classmethod
    def get_all_precatories(cls, db, credor_id=None, numero_precatorio=None, valor_nominal=None, foro=None, data_publicacao=None):
        try:
            query = db.query(cls)

            if credor_id is not None:
                query = query.filter(cls.credor_id == credor_id)
            if numero_precatorio is not None:
                query = query.filter(cls.numero_precatorio == numero_precatorio)
            if valor_nominal is not None:
                query = query.filter(cls.valor_nominal == valor_nominal)
            if foro is not None:
                query = query.filter(cls.foro == foro)
            if data_publicacao is not None:
                query = query.filter(cls.data_publicacao == data_publicacao)

            precatories = query.all()
            return precatories

        except Exception as e:
            print(f"Erro ao buscar precatórios: {e}")
            return None
    
    def __repr__(self):
        return f"Precatory(id={self.id}, credor_id={self.credor_id}, numero_precatorio={self.numero_precatorio}, valor_nominal={self.valor_nominal}, foro={self.foro}, data_publicacao={self.data_publicacao})"
