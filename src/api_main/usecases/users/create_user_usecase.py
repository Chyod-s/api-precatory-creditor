from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.users_model import User
from flask_jwt_extended import create_access_token

class CreateUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, user_name: str, password: str):
        if not user_name or not password:
            raise CustomAPIException("Informe um nome de usuário e uma senha válidos.", 422)

        if User.user_exists(self.db, user_name):
            raise CustomAPIException("Usuário já existe.", 422)

        new_user = User(user_name=user_name, password=password)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        token = create_access_token(identity=str(new_user.id)) 
        return {"token": token, "user_id": new_user.id}
