from flask import Blueprint, request
from src.api_mock.models.creditors import creditors
from src.api_mock.controllers.certificates_controller import search_certificate_by_cpf

certificate_bp = Blueprint('certidao', __name__, url_prefix='/api')

@certificate_bp.route('/certificates', methods=['GET'])
def get_certificate():
    cpf_cnpj = request.args.get('cpf_cnpj')
    
    return search_certificate_by_cpf(cpf_cnpj)

@certificate_bp.route('/creditors', methods=['POST'])
def get_creditors():
    creditors_data = creditors()
    return creditors_data