from enum import Enum

def serialize_certificate(certificate):
    def enum_to_str(value):
        if isinstance(value, Enum):
            return value.value  # pega o valor interno do enum
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
