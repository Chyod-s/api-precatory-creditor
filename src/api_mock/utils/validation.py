from flask import jsonify

def is_valid_cpf(cpf):
    if not cpf:
        return False, (jsonify({"error": "O parâmetro cpf_cnpj é necessário"}), 400)

    if not cpf.isdigit():
        return False, (jsonify({"error": "cpf_cnpj deve conter apenas dígitos"}), 400)

    if cpf != "0" * len(cpf):
        return False, (jsonify({"error": "cpf_cnpj deve ser totalmente zero"}), 400)

    return True, ""
