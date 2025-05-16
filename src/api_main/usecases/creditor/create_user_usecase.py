from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.creditor_model import Creditor

class CreateUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, nome: str, cpf_cnpj: str, email: str, telefone: str, user_id: int):
        if not nome or not cpf_cnpj:
            raise CustomAPIException("Informe um nome e CPF/CNPJ válidos.", 422)
            
        if Creditor.user_exists(self.db, cpf_cnpj):
            raise CustomAPIException("Usuário já existe.", 422)

        new_user = Creditor(nome=nome, cpf_cnpj=cpf_cnpj, email=email, telefone=telefone, user_id=user_id)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return {"user_id": new_user.id}