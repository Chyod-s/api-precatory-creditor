from src.api_main.domain.models.users_model import User
from src.api_main.infraestructure.handler.jwt_handler import generate_token

class CreateUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, user_name: str, password: str):
        if not user_name or not password:
            raise ValueError("Dados inválidos")

        if User.user_exists(self.db, user_name):
            raise ValueError("Usuário já existe")

        new_user = User(user_name=user_name, password=password)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        token = generate_token(user_id=new_user.id)  # type: ignore
        return {"token": token, "user_id": new_user.id}
