from src.api_main.utils.serializers import serialize_creditor, serialize_certificate, serialize_personal_document, serialize_precatory

def aggregated_serialize(data):
    
    serialized_data = {
        "creditors": [serialize_creditor(creditor) for creditor in data.get("creditors", [])],
        "personal_documents": [serialize_personal_document(doc) for doc in data.get("personal_documents", [])],
        "precatory": [serialize_precatory(pre) for pre in data.get("precatory", [])],
        "certificates": data.get("certificates", []),
        "errors": data.get("errors", [])
    }
    return serialized_data
