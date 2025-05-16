from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from src.api_main.usecases.creditor.create_user_usecase import CreateUserUseCase
from src.api_main.infraestructure.database.engine import get_db

def create_creditor():
    db = next(get_db())
    data = request.get_json()
    user_id = get_jwt_identity()
    
    try:
        use_case = CreateUserUseCase(db)
        result = use_case.execute(
            data.get('nome'), 
            data.get('cpf_cnpj'),
            data.get('email'),
            data.get('telefone'),
            user_id
            )

        return jsonify({"status": "success",
                        "message": "Credor criado com sucesso!"
                        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    