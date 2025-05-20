import json
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from src.api_main.aggregator.usecases.aggregate_usecase import AggregateUseCase
from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.infraestructure.database.engine import get_db

def find_aggregate(user_id):
    db = next(get_db())
 
    try:
        data = {"credor_id": user_id}

        aggregator = AggregateUseCase(db)
        aggregated_data = aggregator.aggregate_data(data)

        if not aggregated_data:
            raise CustomAPIException("Nenhum dado encontrado para o usuário.", 404)

        return jsonify({
            "status": "success",
            "data": aggregated_data
        }, 200)

    except CustomAPIException as e:
        return e.to_dict(), e.status_code

    except Exception as e:
        return {
            "status": "error",
            "message": f"Erro ao buscar dados agregados: {str(e)}"
        }, 500
