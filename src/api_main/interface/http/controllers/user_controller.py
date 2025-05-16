from flask import jsonify, request
from src.api_main.domain.models.users_model import User
from src.api_main.infraestructure.database.engine import get_db

def create_user():
    db = next(get_db())
    data = request.get_json()
    new_user = User(user_name=data['user_name'], password=data['password'])
    db.add(new_user)
    db.commit()
    return jsonify({"message": "Usuário criado com sucesso!"}), 201
