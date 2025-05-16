from tabnanny import check
from src.api_main.domain.models.users_model import User
from src.api_main.infraestructure.handler.jwt_handler import generate_token

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

        token = generate_token(user_id=user.id)  # type: ignore

        if not token:
            raise ValueError("Erro ao gerar o token.")
        
        User.att_updated_at(self.db, user)
        
        return {
            "user_name": user.user_name,
            "token": token
        }
