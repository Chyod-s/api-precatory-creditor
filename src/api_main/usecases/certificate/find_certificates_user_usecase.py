from datetime import datetime
from src.api_main.domain.enums.certificate_enum import DataOrigin, DocumentStatus, EntityType
from src.api_main.utils.serializers import serialize_certificate
from src.api_main.domain.models.certificate_model import Certificate
from src.api_main.domain.error.exceptions import CustomAPIException


class FindCertificatesUserUsecase:
    def __init__(self, db):
        self.db = db

    def execute(self, credor_id: int, tipo: EntityType, origem: DataOrigin, arquivo_url: str, status: DocumentStatus, recebida_em: str):
        credor_id = int(credor_id)

        if not isinstance(credor_id, int):
            raise CustomAPIException("ID do credor deve ser um número inteiro.", 422)

        if recebida_em is not None:
            data_publicacao_date = datetime.strptime(recebida_em, '%d/%m/%Y').date()

        certificates = Certificate.get_all_certificates(
            db=self.db,
            credor_id=credor_id,
            tipo=tipo,
            origem=origem,
            arquivo_url=arquivo_url,
            status=status,
            recebida_em=data_publicacao_date if recebida_em else None
        )

        if not certificates:
            raise CustomAPIException("Nenhum certificado encontrado.", 404)

        serialized_certificates = [serialize_certificate(cert) for cert in certificates]

        return serialized_certificates
