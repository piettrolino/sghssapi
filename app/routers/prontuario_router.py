from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.prontuario_model import Prontuario
from app.schemas.prontuario_schema import Prontuario as ProntuarioSchema, ProntuarioCreate

# 1. CORREÇÃO: Remova o prefixo daqui, ele já está no main.py
router = APIRouter(tags=["Prontuários"])

@router.post("/", response_model=ProntuarioSchema)
def criar_prontuario(dados: ProntuarioCreate, db: Session = Depends(get_db)):
    # Nota: Use dados.model_dump() se estiver usando Pydantic v2
    prontuario = Prontuario(**dados.dict())
    db.add(prontuario)
    db.commit()
    db.refresh(prontuario)
    return prontuario

@router.get("/", response_model=list[ProntuarioSchema])
def listar_prontuarios(db: Session = Depends(get_db)):
    return db.query(Prontuario).all()

@router.get("/{id}", response_model=ProntuarioSchema)
def obter_prontuario(id: int, db: Session = Depends(get_db)):
    prontuario = db.query(Prontuario).filter(Prontuario.id == id).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return prontuario

@router.delete("/{id}")
def deletar_prontuario(id: int, db: Session = Depends(get_db)):
    prontuario = db.query(Prontuario).filter(Prontuario.id == id).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    db.delete(prontuario)
    db.commit()
    return {"message": "Prontuário deletado"}