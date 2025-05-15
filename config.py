import os
from dotenv import load_dotenv
from typing import Optional

from api_main.migrations.env import DATABASE_URL

load_dotenv()

DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não está definida.")
