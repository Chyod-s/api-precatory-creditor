from src.api_main.domain.models.personal_document_model import PersonalDocument
from datetime import datetime

class PersonalDocumentUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, credor_id: int, tipo: str, arquivo_url: str, enviado_em: str):
        if not all([credor_id, tipo, arquivo_url, enviado_em]):
            raise ValueError("Dados inválidos")

        data_publicacao_date = datetime.strptime(enviado_em, '%Y-%m-%d').date()

        new_personal_document = PersonalDocument(
            credor_id=credor_id,
            tipo=tipo,
            arquivo_url=arquivo_url,
            enviado_em=data_publicacao_date
        )

        self.db.add(new_personal_document)
        self.db.commit()
        self.db.refresh(new_personal_document)

        return {"personal_document_id": new_personal_document.id}
