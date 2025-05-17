from datetime import datetime
from sqlalchemy import Date
from src.api_main.domain.enums.personal_document_enum import PersonalDocumentEnum
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.personal_document_model import PersonalDocument

class FindPersonalDocumentUserUseCase:
    def __init__(self, db):
        self.db = db
        
    def execute(self, credor_id: int, tipo: PersonalDocumentEnum, enviado_em: str):
        try:
            if enviado_em is not None:
                data_publicacao_date = datetime.strptime(enviado_em, '%d/%m/%Y').date()
            
            personal_documents = PersonalDocument.get_all_personal_documents(
                db=self.db, 
                credor_id=credor_id, 
                tipo=tipo, 
                enviado_em=data_publicacao_date if enviado_em else None)

            if not personal_documents:
                raise CustomAPIException("Documentos pessoais não encontrados.", 404)
                
            return personal_documents
            
        except Exception as e:
            raise CustomAPIException(f"Erro ao buscar documentos pessoais: {str(e)}", 500)
