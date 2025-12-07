from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)

    # 1. CORREÇÃO: Mudar de "patients.id" para "pacientes.id"
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)

    # 2. CORREÇÃO: Mudar de "doctors.id" para "profissionais.id"
    profissional_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)

    data_hora = Column(DateTime, nullable=False)
    motivo = Column(String(255), nullable=True)
    status = Column(String(50), default="agendada")

    # 3. CORREÇÃO: Adicionar back_populates para Patient
    paciente = relationship("Patient", back_populates="consultas")

    # 4. CORREÇÃO: Adicionar back_populates para Doctor
    profissional = relationship("Doctor", back_populates="consultas_agendadas")