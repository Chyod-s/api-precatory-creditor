from src.api_main.usecases.precatory.precatory_user_usecase import CreatePrecatoryUseCase
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.infraestructure.database.engine import get_db

def create_precatory(data):
    db = next(get_db())
    credor_id = data['credor_id']
    
    try:
        use_case = CreatePrecatoryUseCase(db)
        result = use_case.execute(
            numero_precatorio=data.get('numero_precatorio'),
            valor_nominal=data.get('valor_nominal'),
            foro=data.get('foro'),
            data_publicacao=data.get('data_publicacao'),
            credor_id=credor_id
        )
        
        return {"status": "success",
                "message": "Precatorio criado com sucesso!"
                }, 201
    
    except CustomAPIException as e:
        return e.to_dict(), e.status_code
