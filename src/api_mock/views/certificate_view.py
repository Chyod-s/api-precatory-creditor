from flask import Blueprint, request
from src.api_mock.controllers.certificates_controller import search_certificate_by_cpf

certificate_bp = Blueprint('certidao', __name__, url_prefix='/api')

@certificate_bp.route('/certidoes', methods=['GET'])
def get_certificate():
    cpf_cnpj = request.args.get('cpf_cnpj')
    
    return search_certificate_by_cpf(cpf_cnpj)
