from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def init_db(engine):
    from src.api_main.domain.models.creditor_model import Creditor
    from src.api_main.domain.models.precatory_model import Precatory
    from src.api_main.domain.models.personal_document_model import PersonalDocument
    from src.api_main.domain.models.certificate_model import Certificate
    from src.api_main.domain.models.users_model import User
    Base.metadata.create_all(bind=engine)