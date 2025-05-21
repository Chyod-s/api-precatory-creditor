import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../')))

import pytest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.api_main.domain.models.certificate_model import Certificate
from src.api_main.domain.enums.certificate_enum import DocumentStatus, DataOrigin, EntityType
from src.api_main.domain.models.creditor_model import Creditor
from src.api_main.infraestructure.database.base import Base


@pytest.fixture(scope="module")
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_create_certificate(db_session):
    creditor = Creditor(user_id=1, nome="João da Silva", cpf_cnpj="12345678900", email="joao@gmail.com", telefone="123456789")
    db_session.add(creditor)
    db_session.commit()

    certificate = Certificate(
        credor_id=creditor.id, # type: ignore
        tipo=EntityType.LABOR,
        origem=DataOrigin.MANUAL,
        arquivo_url="http://exemplo.com/arquivo.pdf",
        status=DocumentStatus.PENDING,
        recebida_em=date(2024, 1, 1)
    )

    db_session.add(certificate)
    db_session.commit()

    result = db_session.query(Certificate).first()
    assert result is not None
    assert result.credor_id == creditor.id
    assert result.tipo == EntityType.LABOR
    assert result.origem == DataOrigin.MANUAL
    assert result.arquivo_url == "http://exemplo.com/arquivo.pdf"
    assert result.status == DocumentStatus.PENDING
    assert result.recebida_em == date(2024, 1, 1)

def test_get_all_certificates(db_session):
    # Deve retornar o certificado criado acima
    certificates = Certificate.get_all_certificates(db_session)
    assert len(certificates) == 1

    cert = certificates[0]
    assert cert.status == DocumentStatus.PENDING

    # Testando filtro por status
    filtered = Certificate.get_all_certificates(db_session, status=DocumentStatus.PENDING)
    assert len(filtered) == 1

    # Testando filtro com status que não existe
    filtered_none = Certificate.get_all_certificates(db_session, status=DocumentStatus.POSITIVE)
    assert filtered_none == []
