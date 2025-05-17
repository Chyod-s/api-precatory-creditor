from src.api_main.usecases.certificate.find_certificates_user_usecase import FindCertificatesUserUsecase
from src.api_main.usecases.creditor.find_creditor_user_usecase import FindCreditorUserUseCase
from src.api_main.usecases.personal_document.find_personal_document_user_usecase import FindPersonalDocumentUserUseCase
from src.api_main.usecases.precatory.find_precatory_user_usecase import FindPrecatoryUserUseCase
from src.api_main.domain.error.exceptions import CustomAPIException

class AggregateUseCase:
    def __init__(self, db):
        self.db = db

    def aggregate_data(self, data):
        aggregated_data = {
            "creditors": None,
            "personal_documents": None,
            "precatory": None,
            "certificates": None,
            "errors": []
        }

        try:
            creditors = FindCreditorUserUseCase(self.db).execute()
            aggregated_data["creditors"] = creditors
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar credores: {str(e)}")

        try:
            personal_documents = FindPersonalDocumentUserUseCase(self.db).execute(
                credor_id=data["credor_id"],  
                tipo=data.get("tipo"),
                enviado_em=data.get("enviado_em")
            )
            aggregated_data["personal_documents"] = personal_documents
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar documentos pessoais: {str(e)}")

        try:
            precatory = FindPrecatoryUserUseCase(self.db).execute(
                credor_id=data["credor_id"],  
                numero_precatorio=data.get("numero_precatorio"),
                valor_nominal=data.get("valor_nominal"),
                foro=data.get("foro"),
                data_publicacao=data.get("data_publicacao")
            )
            aggregated_data["precatory"] = precatory
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar precatórios: {str(e)}")

        try:
            certificates = FindCertificatesUserUsecase(self.db).execute(
                credor_id=data["credor_id"],  
                tipo=data.get("tipo"),
                origem=data.get("origem"),
                arquivo_url=data.get("arquivo_url"),
                status=data.get("status"),
                recebida_em=data.get("recebida_em")
            )
            aggregated_data["certificates"] = certificates
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar certidões: {str(e)}")

        return aggregated_data
