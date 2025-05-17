from enum import Enum

def serialize_certificate(certificate):
    def enum_to_str(value):
        if isinstance(value, Enum):
            return value.value  
        return str(value)

    def shorten_url(url, max_length=40):
        if len(url) > max_length:
            return url[:max_length] + "..."
        return url
    
    return {
        "id": certificate.id,
        "credor_id": certificate.credor_id,
        "tipo": enum_to_str(certificate.tipo),
        "origem": enum_to_str(certificate.origem),
        "arquivo_url": shorten_url(certificate.arquivo_url),
        "status": enum_to_str(certificate.status),
        "recebida_em": str(certificate.recebida_em),
    }

def serialize_creditor(creditor):
    return {
        "id": creditor.id,
        "nome": creditor.nome,
        "cpf_cnpj": creditor.cpf_cnpj,
        "email": creditor.email,
        "telefone": creditor.telefone
    }

def serialize_personal_document(personal_document):
    def enum_to_str(value):
        if isinstance(value, Enum):
            return value.value  
        return str(value)

    def shorten_url(url, max_length=40):
        if len(url) > max_length:
            return url[:max_length] + "..."
        return url
    
    return {
        "id": personal_document.id,
        "credor_id": personal_document.credor_id,
        "tipo": enum_to_str(personal_document.tipo),
        "arquivo_url": shorten_url(personal_document.arquivo_url),
        "enviado_em": str(personal_document.enviado_em),
    }

def serialize_precatory(precatory):
    return {
        "id": precatory.id,
        "credor_id": precatory.credor_id,
        "numero_precatorio": precatory.numero_precatorio,
        "valor_nominal": precatory.valor_nominal,
        "foro": precatory.foro,
        "data_publicacao": str(precatory.data_publicacao),
    }