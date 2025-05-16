from flask import jsonify
from src.api_mock.utils.validation import is_valid_cpf
from src.api_mock.models.certificate import get_certificate

def search_certificate_by_cpf(cpf_cnpj):
    is_valid, error_response = is_valid_cpf(cpf_cnpj)
    if not is_valid:
        return error_response

    certidao = get_certificate(cpf_cnpj)

    return jsonify(certidao), 200
