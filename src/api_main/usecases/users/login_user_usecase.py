from tabnanny import check
from src.api_main.domain.models.users_model import User
from src.api_main.infraestructure.handler.jwt_handler import generate_token

class LoginUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, user_name: str, password: str):
        if not user_name or not password:
            raise ValueError("Dados inválidos")

        if User.user_exists(self.db, user_name):
            raise ValueError("Usuário já existe")

        check_password = User.check_password(self.db, user_name, password)

        if not check_password:
            raise ValueError("Senha inválida")
        
        token = generate_token(user_id=new_user.id)  # type: ignore
        