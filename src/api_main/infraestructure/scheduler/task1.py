from datetime import datetime, timezone
from src.api_main.domain.models.certificate_model import Certificate
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.infraestructure.database import get_db
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

def my_task(db_session):
    try:
        creditors = Creditor.get_all_creditors(db_session)

        atualizados = []
        nao_atualizados = []

        for creditor in creditors:
            creditor_id = creditor.id
            certificates = Certificate.get_all_certificates(db_session, creditor_id)

            if not certificates:
                continue

            for certificate in certificates:
                if certificate.status.name == "PENDING":
                    certificate.updated_at = datetime.now(tz=timezone.utc)
                    certificate.origem = certificate.origem.API

                    atualizados.append(certificate.id)
                else:
                    nao_atualizados.append(certificate.id)

        db_session.commit()

        logger.info("\n[RESUMO DA TAREFA]")
        logger.info(f"Certidões atualizadas: {len(atualizados)} -> IDs: {atualizados}")
        logger.info(f"Certidões não atualizadas (status diferente de 'PENDING'): {len(nao_atualizados)} -> IDs: {nao_atualizados}")

    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"[ERRO] Falha ao atualizar certificados: {str(e)}")

