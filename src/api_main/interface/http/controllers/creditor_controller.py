from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from src.api_main.usecases.precatory.precatory_user_usecase import CreatePrecatoryUseCase
from src.api_main.usecases.creditor.create_user_usecase import CreateUserUseCase
from src.api_main.infraestructure.database.engine import get_db

def create_creditor():
    db = next(get_db())
    data = request.get_json()
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
                credor_id=user_id
            )
            
        return jsonify({"status": "success",
                        "message": "Credor criado com sucesso!"
                        }), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    