import uuid
import jwt
from datetime import datetime, timedelta, timezone
from src.api_main.config import Config

def generate_token(user_id: int):
    now_utc = datetime.now(timezone.utc)
    payload = {
        'sub': str(user_id),  
        'iat': int(now_utc.timestamp()),  
        'exp': int((now_utc + timedelta(seconds=Config.JWT_EXP_DELTA_SECONDS)).timestamp()),  
        'jti': str(uuid.uuid4()),  
        'type': 'access',  
        'nbf': int(now_utc.timestamp()),  
        'csrf': str(uuid.uuid4()) 
    }
    token = jwt.encode(payload, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    return token


def decode_token(token: str):
    try:
        payload = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM], leeway=10)
        user_id = payload['sub']
        
        # if user_id == "1":
        #     raise Exception("Acesso negado para este usuário.")
        
        return user_id
    except jwt.ExpiredSignatureError:
        raise Exception('Token expirado, faça login novamente.')
    except jwt.InvalidTokenError:
        raise Exception('Token inválido, faça login novamente.')
    