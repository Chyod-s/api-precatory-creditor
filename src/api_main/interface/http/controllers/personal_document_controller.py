from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.usecases.personal_document.personal_document_user_usecase import PersonalDocumentUserUseCase
from src.api_main.infraestructure.database.engine import get_db

def create_personal_document():
    db = next(get_db())
    data = request.get_json()
    user_id = get_jwt_identity()
    
    creditor = Creditor.get_by_id(db, user_id)
    
    if creditor is None:
        return jsonify({"error": "creditor not found!"}), 404

    try:
        use_case = PersonalDocumentUserUseCase(db)
        result = use_case.execute(
            credor_id=creditor.id,
            tipo=data.get('tipo'),
            arquivo_url=data.get('arquivo_url'),
            enviado_em=data.get('enviado_em')
        )

        return jsonify({"status": "success",
                        "message": "Photo document created successfully!",
                        }), 201

    except ValueError as e:
        return {"error": str(e)}, 400