import base64
from flask import request
from werkzeug.datastructures import FileStorage
from flask_jwt_extended import get_jwt_identity
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.usecases.personal_document.personal_document_user_usecase import PersonalDocumentUserUseCase
from src.api_main.infraestructure.database.engine import get_db

def create_personal_document(data):
    db = next(get_db())
    user_id = get_jwt_identity()
    
    try:
        creditor = Creditor.get_by_id(db, user_id)
    
        if creditor is None:
            raise CustomAPIException("Credor não encontrado", 404)
    
        file = request.files.get('arquivo_url')
    
        if not isinstance(file, FileStorage):
            raise CustomAPIException("Formato inválido ou arquivo não encontrado", 422)
            
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
        
        use_case = PersonalDocumentUserUseCase(db)
        result = use_case.execute(
            credor_id=creditor.id,
            tipo=data.get('tipo'),
            arquivo_url=encoded_string,
            enviado_em=data.get('enviado_em')
        )

        return {"status": "success",
                "message": "Photo document created successfully!",
                }, 201

    except CustomAPIException as e:
        return e.to_dict(), e.status_code
    