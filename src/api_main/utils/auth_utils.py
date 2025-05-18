from datetime import datetime, timezone
import jwt

from src.api_main.config import Config

lol = Config()

SECRET_KEY = lol.JWT_SECRET_KEY

def validate_jwt_token(token):
    try:
        now = datetime.now(timezone.utc)
        print(f"Validando token no servidor - now (UTC): {now}")
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print(f"Token válido: {payload}")
        return payload
    except jwt.ExpiredSignatureError as e:
        print(f"Erro: Token expirado: {e}")
        return None
    except jwt.InvalidTokenError as e:
        print(f"Erro: Token inválido: {e}")
        return None
