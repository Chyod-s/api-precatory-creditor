from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.creditor_model import Creditor

class CreateUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, nome: str, cpf_cnpj: str, email: str, telefone: str, user_id):
        if isinstance(user_id, str):
            try:
                user_id = int(user_id.replace(',', ''))
            except ValueError:
                raise CustomAPIException("user_id deve ser um número válido.", 422)

        if not isinstance(user_id, int):
            raise CustomAPIException("user_id deve ser um número.", 422)

        if not nome or not cpf_cnpj:
            raise CustomAPIException("Informe um nome e CPF/CNPJ válidos.", 421)

        if Creditor.user_exists(self.db, cpf_cnpj):
            raise CustomAPIException("Usuário já existe.", 423)

        new_user = Creditor(nome=nome, cpf_cnpj=cpf_cnpj, email=email, telefone=telefone, user_id=user_id)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return {"user_id": new_user.id}
