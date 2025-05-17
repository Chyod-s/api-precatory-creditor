from src.api_main.domain.enums.personal_document_enum import PersonalDocumentEnum
from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

class PersonalDocument(BaseModel):
    __tablename__ = "documento_pessoal"
    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey("credor.id"), nullable=False)
    tipo = Column(Enum(PersonalDocumentEnum), nullable=False, default=PersonalDocumentEnum.ETC)
    arquivo_url = Column(String, nullable=True)
    enviado_em = Column(Date, nullable=True)

    creditor = relationship("Creditor", back_populates="personal_documents")

    def __init__(self, credor_id, tipo, arquivo_url, enviado_em): 
        self.credor_id = credor_id
        self.tipo = tipo
        self.arquivo_url = arquivo_url
        self.enviado_em = enviado_em

    def __repr__(self):
        return f"PersonalDocument(id={self.id}, credor_id={self.credor_id}, tipo={self.tipo.name}, arquivo_url={self.arquivo_url}, enviado_em={self.enviado_em})"
