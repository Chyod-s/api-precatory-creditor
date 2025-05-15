from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def init_db(engine):
    from src.api_main.domain.models import Base
    Base.metadata.create_all(bind=engine)   