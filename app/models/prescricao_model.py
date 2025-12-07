from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.database import Base

class Prescricao(Base):
    __tablename__ = "prescricoes"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)
    texto = Column(String(500), nullable=False)
    data = Column(DateTime, default=datetime.now)
