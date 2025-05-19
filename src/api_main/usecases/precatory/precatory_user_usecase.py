from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.precatory_model import Precatory
from datetime import datetime

class CreatePrecatoryUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, numero_precatorio: str, valor_nominal, foro: str, data_publicacao, credor_id: int):
        data_publicacao_date = None
        
        if not numero_precatorio:
            raise CustomAPIException("Número do precatório é obrigatório.", 422)

        if isinstance(valor_nominal, str):
            try:
                valor_nominal = float(valor_nominal.replace(',', '.'))
            except ValueError:
                raise CustomAPIException("Valor nominal deve ser um número válido.", 422)

        if not isinstance(valor_nominal, (int, float)):
            raise CustomAPIException("Valor nominal deve ser um número.", 422)

        if "-" in data_publicacao:
            try:
                data_publicacao_date = datetime.strptime(data_publicacao, '%d-%m-%Y').date()
                print(f"A data está no formato correto: {data_publicacao_date.strftime('%d/%m/%Y')}")
            except ValueError:
                try:
                    data_publicacao_date = datetime.strptime(data_publicacao, '%Y-%m-%d').date()
                    print(f"A data está no formato correto: {data_publicacao_date.strftime('%d/%m/%Y')}")
                except ValueError:
                    print("A data NÃO está em um formato válido.")
      
        elif isinstance(data_publicacao, datetime):
            data_publicacao_date = data_publicacao.date()
        else:
            raise CustomAPIException("Data de publicação inválida.", 422)
            
        if not foro:
            raise CustomAPIException("Foro é obrigatório.", 422)

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
