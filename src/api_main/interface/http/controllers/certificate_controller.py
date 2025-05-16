import base64
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from werkzeug.datastructures import FileStorage
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.usecases.certificate.certificate_user_usecase import CertificateUserUseCase
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.infraestructure.database.engine import get_db

def certificate_personal_document(data):
    db = next(get_db())
    user_id = get_jwt_identity()

    try:

        creditor = Creditor.get_by_id(db, user_id)
        if creditor is None:
            raise CustomAPIException("Credor não encontrado.", 404)

        file = data.get('arquivo_url')

        if not isinstance(file, FileStorage):
            raise CustomAPIException("Arquivo inválido.", 422)

        encoded_string = base64.b64encode(file.read()).decode('utf-8')

        use_case = CertificateUserUseCase(db)
        result = use_case.execute(
            credor_id=creditor.id,
            tipo=data.get('tipo'),
            origem=data.get('origem'),
            arquivo_url=encoded_string,
            status=data.get('status'),
            recebida_em=data.get('recebida_em')
        )

        return {"status": "success",
                "message": "Documento enviado com sucesso!",
                "data": result}, 201

    except CustomAPIException as e:
        return e.to_dict(), e.status_code
