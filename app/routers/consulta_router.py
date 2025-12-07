from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.consulta_model import Consulta
from app.schemas.consulta_schema import ConsultaCreate, ConsultaOut, ConsultaUpdate

# 1. CORREÇÃO: Remova o prefixo daqui, ele já está no main.py
router = APIRouter(tags=["Consultas"])

@router.post("/", response_model=ConsultaOut)
def create_consulta(data: ConsultaCreate, db: Session = Depends(get_db)):
    # Nota: Em versões mais recentes do Pydantic, use data.model_dump()
    consulta = Consulta(**data.dict())
    db.add(consulta)
    db.commit()
    db.refresh(consulta)
    return consulta

@router.get("/{consulta_id}", response_model=ConsultaOut)
def get_consulta(consulta_id: int, db: Session = Depends(get_db)):
    consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
    if not consulta:
        raise HTTPException(404, detail="Consulta não encontrada")
    return consulta