from src.api_main.domain.enums.certificate_enum import DocumentStatus, DataOrigin, EntityType
from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from datetime import date


class Certificate(BaseModel):
    __tablename__ = "certidao"
    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey("credor.id"), nullable=False)
    tipo = Column(Enum(EntityType), nullable=False, default=EntityType.LABOR)
    origem = Column(Enum(DataOrigin), nullable=False, default=DataOrigin.MANUAL)
    arquivo_url = Column(String, nullable=True)
    status = Column(Enum(DocumentStatus), nullable=False, default=DocumentStatus.PENDING)
    recebida_em = Column(Date, nullable=True)

    creditor = relationship("Creditor", back_populates="certificates")

    def __init__(self, credor_id: int, tipo: EntityType, origem: DataOrigin, arquivo_url: str, status: DocumentStatus, recebida_em: date):
        self.credor_id = credor_id
        self.tipo = tipo
        self.origem = origem
        self.arquivo_url = arquivo_url
        self.status = status
        self.recebida_em = recebida_em

    @classmethod
    def get_all_certificates(cls, db, credor_id=None, tipo=None, origem=None, arquivo_url=None, status=None, recebida_em=None):
        try:
            query = db.query(cls)

            if credor_id is not None:
                query = query.filter(cls.credor_id == credor_id)
            if tipo is not None:
                query = query.filter(cls.tipo == tipo)
            if origem is not None:
                query = query.filter(cls.origem == origem)
            if arquivo_url is not None:
                query = query.filter(cls.arquivo_url == arquivo_url)
            if status is not None:
                query = query.filter(cls.status == status)
            if recebida_em is not None:
                query = query.filter(cls.recebida_em == recebida_em)

            certificates = query.all()
            return certificates
        
        except Exception as e:
            print(f"Erro ao buscar certificados: {e}")
            return []


    def __repr__(self):
        return f"Certificate(id={self.id}, credor_id={self.credor_id}, tipo={self.tipo}, origem={self.origem}, arquivo_url={self.arquivo_url}, status={self.status}, recebida_em={self.recebida_em})"
    