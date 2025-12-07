from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.patient_model import Patient
from app.schemas.patient_schema import PatientCreate, PatientResponse

# 1. CORREÇÃO: Remova o prefixo daqui, ele já está no main.py
router = APIRouter(tags=["Pacientes"])

@router.post("/", response_model=PatientResponse)
def create_patient(data: PatientCreate, db: Session = Depends(get_db)):
    # Nota: Use data.model_dump() se estiver usando Pydantic v2
    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return patient