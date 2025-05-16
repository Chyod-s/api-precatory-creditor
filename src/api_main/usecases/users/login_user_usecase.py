from src.api_main.domain.models.users_model import User
from flask_jwt_extended import create_access_token

class LoginUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, user_name: str, password: str):
        if not user_name or not password:
            raise ValueError("Nome de usuário e senha são obrigatórios.")

        user = User.get_user(self.db, user_name)
        if not user:
            raise ValueError("Usuário não encontrado.")

        if not user.check_password(user.password,password):
            raise ValueError("Senha inválida.")

        token = create_access_token(identity=str(user.id)) 

        if not token:
            raise ValueError("Erro ao gerar o token.")
        
        User.att_updated_at(self.db, user)
        
        return {
            "user_name": user.user_name,
            "token": token
        }
