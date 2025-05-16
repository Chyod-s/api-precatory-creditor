from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.users_model import User
from flask_jwt_extended import create_access_token

class LoginUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, user_name: str, password: str):
        if not user_name or not password:
            raise CustomAPIException("Informe um nome de usuário e uma senha válidos.", 422)
            
        user = User.get_user(self.db, user_name)
        if not user:
            raise CustomAPIException("Usuário não encontrado.", 422)

        if not user.check_password(user.password,password):
            raise CustomAPIException("Senha inválida.", 422)

        token = create_access_token(identity=str(user.id)) 

        if not token:
            raise ValueError("Erro ao gerar o token.")
        
        User.att_updated_at(self.db, user)
        
        return {
            "user_name": user.user_name,
            "token": token
        }
