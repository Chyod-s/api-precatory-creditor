from src.api_main.domain.models.precatory_model import Precatory
from datetime import datetime

class CreatePrecatoryUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, numero_precatorio: str, valor_nominal: float, foro: str, data_publicacao: str, credor_id: int):
        if not all([numero_precatorio, valor_nominal, foro, data_publicacao]):
                raise ValueError("Dados inválidos")

        if not isinstance(valor_nominal, (int, float)):
            raise ValueError("Valor nominal deve ser um número")

        data_publicacao_date = datetime.strptime(data_publicacao, '%Y-%m-%d').date()

        new_precatory = Precatory(
            numero_precatorio=numero_precatorio,
            valor_nominal=valor_nominal,
            foro=foro,
            data_publicacao=data_publicacao_date,
            credor_id=credor_id
        )

        self.db.add(new_precatory)
        self.db.commit()
        self.db.refresh(new_precatory)

        return {"precatory_id": new_precatory.id}
    