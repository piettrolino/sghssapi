from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
SECRET_KEY = "SUA_CHAVE_SECRETA"

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)

def gerar_token(payload: dict, exp_minutos: int = 60) -> str:
    data = payload.copy()
    data["exp"] = datetime.utcnow() + timedelta(minutes=exp_minutos)
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")
