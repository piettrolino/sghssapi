from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Prontuario(Base):
    __tablename__ = "prontuarios"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)
    descricao = Column(String(500), nullable=False)
    diagnostico = Column(String(300), nullable=False)
    prescricao = Column(String(300), nullable=False)
    data_hora = Column(DateTime, default=datetime.now)

    # CORREÇÃO: Adicione o back_populates
    # O "pacientes" deve ser o nome do atributo de lista definido no Model Patient
    paciente = relationship("Patient", back_populates="prontuarios")

    # CORREÇÃO: Adicione o back_populates
    # O "prontuarios" deve ser o nome do atributo de lista definido no Model Doctor
    profissional = relationship("Doctor", back_populates="prontuarios_atendidos")