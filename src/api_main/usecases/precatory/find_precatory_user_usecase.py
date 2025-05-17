from datetime import datetime
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.precatory_model import Precatory

class FindPrecatoryUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, credor_id: int, numero_precatorio: str, valor_nominal: float, foro: str, data_publicacao: str):
        credor_id = int(credor_id)
   
        if not isinstance(credor_id, int):
            raise CustomAPIException("ID do credor deve ser um número inteiro.", 422)

        if data_publicacao is not None:
                data_publicacao_date = datetime.strptime(data_publicacao, '%d/%m/%Y').date()

        precatory = Precatory.get_all_precatories(
            db=self.db,
            credor_id=credor_id,
            numero_precatorio=numero_precatorio,
            valor_nominal=valor_nominal,
            foro=foro,
            data_publicacao=data_publicacao_date if data_publicacao else None
        )

        if not precatory:
            raise CustomAPIException("Precatórios não encontrados.", 404)

        return precatory
