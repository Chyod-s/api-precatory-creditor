from flask_jwt_extended import get_jwt_identity
from src.api_main.usecases.creditor.find_creditor_user_usecase import FindCreditorUserUseCase
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.usecases.precatory.precatory_user_usecase import CreatePrecatoryUseCase
from src.api_main.usecases.creditor.create_user_usecase import CreateUserUseCase
from src.api_main.infraestructure.database.engine import get_db
from itertools import chain

def create_creditor(data):
    db = next(get_db())
    user_id = get_jwt_identity()
    
    try:
        use_case = CreateUserUseCase(db)
        result = use_case.execute(
            data.get('nome'), 
            data.get('cpf_cnpj'),
            data.get('email'),
            data.get('telefone'),
            user_id
            )
        
        if 'precatorio' in data:
            precatory_data = data['precatorio']
            precatory_use_case = CreatePrecatoryUseCase(db)
            precatory_result = precatory_use_case.execute(
                numero_precatorio=precatory_data.get('numero_precatorio'),
                valor_nominal=precatory_data.get('valor_nominal'),
                foro=precatory_data.get('foro'),
                data_publicacao=precatory_data.get('data_publicacao'),
                credor_id=result['user_id'] # type: ignore
            )
            
        return {"status": "success",
                "message": "Credor criado com sucesso!"
                }, 201
    
    except CustomAPIException as e:
        return e.to_dict(), e.status_code

def get_creditor(user_id):
    db = next(get_db())

    try:
        use_case = FindCreditorUserUseCase(db)
        result = use_case.get_creditor_by_id(user_id)

        precatories = [
            p for i in result for p in i.precatories if p.numero_precatorio != '0'
        ]
        flattened_precatories = list(precatories)

        if not result:
            raise CustomAPIException("Credores não encontrados.", 404)
        
        list_creditors_precatories = []
        for i in range(len(result)):
            list_creditors_precatories.append(creditor_to_dict(result[i], flattened_precatories))
            
        return list_creditors_precatories, 200

    except CustomAPIException as e:
        return e.to_dict(), e.status_code


def creditor_to_dict(creditor, precatories=None):
    return {
        "id": creditor.id,
        "nome": creditor.nome,
        "cpf_cnpj": creditor.cpf_cnpj,
        "email": creditor.email,
        "telefone": creditor.telefone,
        "precatorios": [
            {
                "numero_precatorio": p.numero_precatorio,
                "valor_nominal": p.valor_nominal,
                "foro": p.foro,
                "data_publicacao": str(p.data_publicacao)
            }
            for p in precatories
        ] if precatories else []
    }

