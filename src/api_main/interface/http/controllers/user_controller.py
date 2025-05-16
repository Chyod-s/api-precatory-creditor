from flask import jsonify, request
from src.api_main.infraestructure.database.engine import get_db
from src.api_main.usecases.users.create_user_usecase import CreateUserUseCase

def create_user():
    db = next(get_db())
    data = request.get_json()

    try:
        use_case = CreateUserUseCase(db)
        result = use_case.execute(data.get('user_name', ''), data.get('password', ''))

        return jsonify({"status": "success",
                        "message": "Usuário criado com sucesso!",
                        "data": result}), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
