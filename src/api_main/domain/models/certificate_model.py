from src.api_main.domain.enums.certificate_enum import DocumentStatus, DataOrigin, EntityType
from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, Date, Integer, String, Enum
from sqlalchemy.orm import relationship

class Certificate(BaseModel):
    __tablename__ = "certidao"
    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, nullable=False)
    tipo = Column(Enum(EntityType), nullable=False, default=EntityType.LABOR)
    origem = Column(Enum(DataOrigin), nullable=False, default=DataOrigin.MANUAL)
    arquivo_url = Column(String, nullable=True)
    status = Column(Enum(DocumentStatus), nullable=False, default=DocumentStatus.PENDING)
    recebida_em = Column(Date, nullable=True)

    creditor = relationship("Creditor", back_populates="certificates")

    __doc__ = "Modelo de Certidão"
    id.__doc__ = "ID da certidão"
    credor_id.__doc__ = "ID do credor"
    tipo.__doc__ = "Tipo da certidão"
    origem.__doc__ = "Origem da certidão"
    arquivo_url.__doc__ = "URL do arquivo da certidão"
    status.__doc__ = "Status da certidão"
    recebida_em.__doc__ = "Data de recebimento da certidão"
    def __repr__(self):
        return f"Certificate(id={self.id}, credor_id={self.credor_id}, tipo={self.tipo}, origem={self.origem}, arquivo_url={self.arquivo_url}, status={self.status}, recebida_em={self.recebida_em})"
    