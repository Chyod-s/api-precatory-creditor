from flask import jsonify, request
from src.api_main.usecases.users.login_user_usecase import LoginUserUseCase
from src.api_main.infraestructure.database.engine import get_db
from src.api_main.usecases.users.create_user_usecase import CreateUserUseCase

def create_user(data):
    db = next(get_db())
    try:
        use_case = CreateUserUseCase(db)
        result = use_case.execute(data.get('user_name', ''), data.get('password', ''))

        return {"status": "success",
                        "message": "Usuário criado com sucesso!",
                        "data": result}, 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def get_user():
    db = next(get_db())
    data = request.get_json()

    try:
        use_case = LoginUserUseCase(db)
        result = use_case.execute(data.get('user_name'), data.get('password'))

        return {"status": "success",
                        "message": "Usuário encontrado com sucesso!",
                        "data": result}, 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400