import token
from tokenize import String
from flask import jsonify, request
from src.api_main.domain.models.users_model import User
from src.api_main.infraestructure.database.engine import get_db
from src.api_main.infraestructure.jwt.jwt_handler import generate_token, decode_token


def create_user():
    db = next(get_db())
    data = request.get_json()
    
    user_name = data.get('user_name', '')
    password = data.get('password', '')

    if not user_name or not password:
        return jsonify({"error": "Dados inválidos"}), 400

    if User.user_exists(db, user_name):
        return jsonify({"error": "Usuário já existe"}), 400

    new_user = User(user_name=data['user_name'], password=data['password'])

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = generate_token(user_id=new_user.id)  # type: ignore

    return jsonify({"status": "success",
                    "message": "Usuário criado com sucesso!",
                    "data": {
                        "token": token
                    }}), 201
