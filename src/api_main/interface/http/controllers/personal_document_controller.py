import base64
from flask import request
from werkzeug.datastructures import FileStorage
from flask_jwt_extended import get_jwt_identity
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.usecases.personal_document.personal_document_user_usecase import PersonalDocumentUserUseCase
from src.api_main.infraestructure.database.engine import get_db
from src.api_main.config import Config

def create_personal_document(data):
    db = next(get_db())
    user_id = get_jwt_identity()
    
    try:
        creditor = Creditor.get_by_id(db, user_id)
    
        if creditor is None:
            raise CustomAPIException("Credor não encontrado", 404)
    
        def is_valid_extension(filename):
            return any(filename.lower().endswith(ext) for ext in Config.ALLOWED_EXTENSIONS)

        def is_valid_size(file):
            file.seek(0, 2)  
            file_size = file.tell()
            file.seek(0)  
            return file_size <= Config.MAX_FILE_SIZE

        file = data.get('arquivo_url')

        if not isinstance(file, FileStorage):
            raise CustomAPIException("Arquivo inválido.", 422)

        if not is_valid_extension(file.filename):
            raise CustomAPIException("Extensão de arquivo não permitida.", 422)

        if not is_valid_size(file):
            raise CustomAPIException("Arquivo excede o tamanho máximo permitido.", 422)

        encoded_string = base64.b64encode(file.read()).decode('utf-8')
        
        use_case = PersonalDocumentUserUseCase(db)
        result = use_case.execute(
            credor_id=int(data.get('credor_id')),
            tipo=data.get('tipo'),
            arquivo_url=encoded_string,
            enviado_em=data.get('enviado_em')
        )

        return {"status": "success",
                "message": "Documento registrado com sucesso!",
                }, 201

    except CustomAPIException as e:
        return e.to_dict(), e.status_code
    