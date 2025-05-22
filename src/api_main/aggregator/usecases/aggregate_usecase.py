from src.api_main.domain.models.certificate_model import Certificate
from src.api_main.domain.models.precatory_model import Precatory
from src.api_main.domain.models.personal_document_model import PersonalDocument
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.domain.error.exceptions import CustomAPIException
import src.api_main.utils.aggregated_serialize as serialize

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
            creditors = Creditor.get_by_id(self.db, data["credor_id"])

            result = []
            
            for c in creditors:
                result.append({
                    "nome": c.nome,
                    "cpf_cnpj": c.cpf_cnpj,
                    "email": c.email,
                    "telefone": c.telefone,
                })

            aggregated_data["creditors"] = result
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar credores: {str(e)}")

        try:
            personal_documents = PersonalDocument.get_all_personal_documents(
                db=self.db, 
                credor_id=data["credor_id"]) or []

            result = []

            for doc in personal_documents:
                tipo_name = doc.tipo.name if doc.tipo else None
                arquivo_url = doc.arquivo_url if doc.arquivo_url else None
                enviado_em = doc.enviado_em if doc.enviado_em else None

                arquivo_url_slice = (arquivo_url[:25] + "...") if arquivo_url and len(arquivo_url) > 25 else arquivo_url

                result.append({
                    "tipo": tipo_name,
                    "arquivo_url": arquivo_url_slice,
                    "enviado_em": enviado_em
                })

            aggregated_data["personal_documents"] = result
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar documentos pessoais: {str(e)}")

        try:
            precatory = Precatory.get_all_precatories(
                db=self.db,
                credor_id=data["credor_id"]) or []
            
            result = []

            for doc in precatory:
                numero_precatorio = doc.numero_precatorio if doc.numero_precatorio else None
                valor_nominal = doc.valor_nominal if doc.valor_nominal else None
                foro = doc.foro if doc.foro else None
                data_publicacao = doc.data_publicacao if doc.data_publicacao else None

                if (
                        numero_precatorio == "0"
                        and valor_nominal is None
                        and data_publicacao
                        and data_publicacao.year == 2000
                    ):
                        continue
                
                result.append({
                    "numero_precatorio": numero_precatorio,
                    "valor_nominal": valor_nominal,
                    "foro": foro,
                    "data_publicacao": data_publicacao
                })

            aggregated_data["precatory"] = result
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar precatórios: {str(e)}")

        try:
            certificates = Certificate.get_all_certificates(
                db=self.db,
                credor_id=data["credor_id"] 
            ) or []

            result = []

            for doc in certificates:
                tipo = doc.tipo.name if doc.tipo else None
                origem = doc.origem.name if doc.origem else None
                arquivo_url = doc.arquivo_url if doc.arquivo_url else None
                status = doc.status.name if doc.status else None
                recebida_em = doc.recebida_em if doc.recebida_em else None

                arquivo_url_slice = (arquivo_url[:25] + "...") if arquivo_url and len(arquivo_url) > 25 else arquivo_url

                result.append({
                    "tipo": tipo,
                    "origem": origem,
                    "arquivo_url": arquivo_url_slice,
                    "status": status,
                    "recebida_em": recebida_em
                })

            aggregated_data["certificates"] = result
        except CustomAPIException as e:
            aggregated_data["errors"].append(f"Erro ao buscar certidões: {str(e)}")

        return aggregated_data
    