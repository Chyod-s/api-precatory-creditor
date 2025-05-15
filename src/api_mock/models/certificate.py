
def get_certificate(cpf_cnpj):
    if not cpf_cnpj:
        return None

    certidao = {
        "cpf_cnpj": cpf_cnpj,
        "certidoes": [
            {
                "tipo": "federal",
                "status": "negativa",
                "conteudo_base64": "..."
            },
            {
                "tipo": "trabalhista",
                "status": "positiva",
                "conteudo_base64": "..."
            }
        ]
    }
    return certidao
