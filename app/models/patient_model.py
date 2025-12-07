# app/models/patient_model.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Patient(Base):
    __tablename__ = "pacientes"  # Nome certo

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255), unique= True, nullable=False)

    # RELACIONAMENTOS
    prontuarios = relationship("Prontuario", back_populates="paciente")
    consultas = relationship("Consulta", back_populates="paciente")