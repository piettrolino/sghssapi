# app/routers/leito_router.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.leito_model import Leito
from app.schemas.leito_schema import LeitoCreate, Leito

router = APIRouter(prefix="/leitos", tags=["Leitos"])

# ROTA DE REGISTRO (POST) - Para criar novos leitos
@router.post("/", response_model=Leito, status_code=status.HTTP_201_CREATED)
def registrar_leito(leito: LeitoCreate, db: Session = Depends(get_db)):
    # ... (código de criação de leito aqui) ...
    db_leito = Leito(
        tipo=leito.tipo,
        status=leito.status
    )
    db.add(db_leito)
    db.commit()
    db.refresh(db_leito)
    return db_leito

# 🚨 ROTA DE LISTAGEM (GET) - ESSA É A ROTA QUE VOCÊ ESTÁ TENTANDO ACESSAR!
@router.get("/", response_model=list[Leito])
def listar_leitos(db: Session = Depends(get_db)):
    """Lista todos os leitos registrados no sistema."""
    return db.query(Leito).all()

# ROTA DE BUSCA POR ID (GET/{id})
@router.get("/{leito_id}", response_model=Leito)
def buscar_leito(leito_id: int, db: Session = Depends(get_db)):
    leito = db.query(Leito).filter(Leito.id == leito_id).first()
    if leito is None:
        raise HTTPException(status_code=404, detail="Leito não encontrado")
    return leito