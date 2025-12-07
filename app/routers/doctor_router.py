from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.doctor_model import Doctor
from app.schemas.doctor_schema import DoctorCreate, DoctorResponse

# 1. CORREÇÃO: Remova o prefixo daqui, ele já está no main.py
router = APIRouter(tags=["Médicos"])

@router.post("/", response_model=DoctorResponse)
def create_doctor(data: DoctorCreate, db: Session = Depends(get_db)):
    exists = db.query(Doctor).filter(Doctor.crm == data.crm).first()
    if exists:
        raise HTTPException(400, detail="CRM já cadastrado.")
    # Nota: Use data.model_dump() se estiver usando Pydantic v2
    doctor = Doctor(**data.dict())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(404, detail="Médico não encontrado")
    return doctor