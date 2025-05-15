from api_main.domain.enums.personal_document_enum import PersonalDocumentEnum
from .base_model import BaseModel
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

class PersonalDocument(BaseModel):
    __tablename__ = "documento_pessoal"
    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey("credor.id"), nullable=False)
    tipo = Column(Enum(PersonalDocumentEnum), nullable=False, default=PersonalDocumentEnum.etc)
    arquivo_url = Column(String, nullable=True)
    enviado_em = Column(Date, nullable=True)

    creditor = relationship("Creditor", back_populates="personal_documents")

    __doc__ = "Modelo de Documento Pessoal"
    id.__doc__ = "ID do documento pessoal"
    credor_id.__doc__ = "ID do credor"
    tipo.__doc__ = "Tipo do documento pessoal"
    arquivo_url.__doc__ = "URL do arquivo do documento pessoal"
    enviado_em.__doc__ = "Data de envio do documento pessoal"

    def __repr__(self):
        return f"PersonalDocument(id={self.id}, credor_id={self.credor_id}, tipo={self.tipo.name}, arquivo_url={self.arquivo_url}, enviado_em={self.enviado_em})"
