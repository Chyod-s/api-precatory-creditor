import os
import sys
from logging.config import fileConfig
from sqlalchemy import pool, create_engine
from alembic import context
from dotenv import load_dotenv

# Adiciona a raiz do projeto ao sys.path para importar os modelos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

load_dotenv()

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa o Base dos seus modelos
from api_main.domain.models import Base

target_metadata = Base.metadata

# Define o caminho para o banco dentro da pasta data (dentro da pasta migrations)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
os.makedirs(BASE_DIR, exist_ok=True)  # Cria se não existir

DB_PATH = os.path.join(BASE_DIR, 'precatory-creditor.db')
DATABASE_URL = os.getenv("DATABASE_URL")



def run_migrations_offline() -> None:
    """Executa as migrações no modo offline."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa as migrações no modo online."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
