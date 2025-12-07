from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

from app.models.user_model import User
# 🚨 MUDANÇA AQUI: Importar UsuarioOut no lugar de Usuario
from app.schemas.user_schema import UsuarioOut, UsuarioCreate
from app.utils.security import hash_senha, verificar_senha, gerar_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/register", response_model=UsuarioOut) # <--- response_model CORRIGIDO
def registrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # 1. Checagem: Verifique se o email já existe
    if db.query(User).filter(User.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="E-mail já registrado.")

    hashed = hash_senha(usuario.senha)

    user = User(
        nome=usuario.nome,
        email=usuario.email,
        # O campo 'senha' no Model do SQLAlchemy é onde o hash é salvo.
        senha=hashed,
        perfil=usuario.perfil
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login")
# 3. Nota: Para receber dados de login via JSON Body (melhor prática),
# é recomendado usar um Schema Pydantic para Login (ex: LoginSchema) aqui.
def login(email: str, senha: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user or not verificar_senha(senha, user.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = gerar_token({"id": user.id, "perfil": user.perfil})

    return {"access_token": token, "tipo": "Bearer"}