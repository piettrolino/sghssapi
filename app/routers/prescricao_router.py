from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.prescricao_model import Prescricao
from app.schemas.prescricao_schema import Prescricao, PrescricaoCreate

# 1. CORREÇÃO: Remova o prefixo daqui, ele já está no main.py
router = APIRouter(tags=["Prescrições"])

@router.post("/", response_model=Prescricao)
def criar_prescricao(dados: PrescricaoCreate, db: Session = Depends(get_db)):
    # Nota: Em versões mais recentes do Pydantic, use dados.model_dump()
    p = Prescricao(**dados.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

@router.get("/", response_model=list[Prescricao])
def listar_prescricoes(db: Session = Depends(get_db)):
    return db.query(Prescricao).all()