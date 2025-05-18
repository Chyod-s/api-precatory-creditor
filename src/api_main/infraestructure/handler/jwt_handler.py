from zoneinfo import ZoneInfo
import jwt
from datetime import datetime, timedelta
from src.api_main.config import Config

campo_grande_tz = ZoneInfo("America/Campo_Grande")

def generate_token(user_id: int):
    now_cg = datetime.now(tz=campo_grande_tz)
    now_utc = now_cg.astimezone(ZoneInfo("UTC"))
    
    payload = {
        'user_id': user_id,
        'iat': now_utc,
        'exp': now_utc + timedelta(seconds=Config.JWT_EXP_DELTA_SECONDS),
    }

    token = jwt.encode(payload, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    return token

def decode_token(token: str):
    try:
        payload = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        raise Exception('Token expirado, faça login novamente.')
    except jwt.InvalidTokenError:
        raise Exception('Token inválido, faça login novamente.')
