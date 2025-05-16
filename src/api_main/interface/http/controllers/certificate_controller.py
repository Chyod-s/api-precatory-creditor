import base64
from datetime import datetime
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from werkzeug.datastructures import FileStorage
from src.api_main.usecases.certificate.certificate_user_usecase import CertificateUserUseCase
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.infraestructure.database.engine import get_db

def certificate_personal_document():
    db = next(get_db())
    data = request.get_json()
    user_id = get_jwt_identity()
    
    creditor = Creditor.get_by_id(db, user_id)
    if creditor is None:
        return jsonify({"error": "creditor not found!"}), 404
    
    try:
    
        file = request.files.get('arquivo_url')
    
        if not isinstance(file, FileStorage):
            return jsonify({"error": "File not found or invalid format"}), 400

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

        return jsonify({"status": "success",
                        "message": "Photo document created successfully!",
                        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
