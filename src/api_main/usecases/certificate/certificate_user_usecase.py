from datetime import datetime
from sqlalchemy import String
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.enums.certificate_enum import DataOrigin, DocumentStatus, EntityType
from src.api_main.domain.models.certificate_model import Certificate


class CertificateUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, credor_id: int, tipo: EntityType, origem: DataOrigin, arquivo_url: str, status: DocumentStatus, recebida_em: str):
        if not all([credor_id, tipo, origem, arquivo_url, status, recebida_em]):
            raise CustomAPIException("Dados inválidos.", 422)
            

        data_publicacao_date = datetime.strptime(recebida_em, '%Y-%m-%d').date()
        
        new_certificate = Certificate(
            credor_id=credor_id,
            tipo=tipo,
            origem=origem,
            arquivo_url=arquivo_url,
            status=status,
            recebida_em=data_publicacao_date
        )

        self.db.add(new_certificate)
        self.db.commit()
        self.db.refresh(new_certificate)

        return {"certificate_id": new_certificate.id}
    