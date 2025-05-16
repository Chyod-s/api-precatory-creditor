from flask import jsonify, request
from src.api_main.usecases.creditor.create_user_usecase import CreateUserUseCase
from src.api_main.infraestructure.database.engine import get_db

def create_creditor():
    db = next(get_db())
    data = request.get_json()

    try:
        use_case = CreateUserUseCase(db)
        result = use_case.execute(
            data.get('nome'), 
            data.get('cpf_cnpj'),
            data.get('email'),
            data.get('telefone')
            )

        return jsonify({"status": "success",
                        "message": "Credor criado com sucesso!"
                        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    