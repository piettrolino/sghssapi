from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from datetime import datetime
from app.database import Base

class Teleconsulta(Base):
    __tablename__ = "teleconsultas"

    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)
    link_sessao = Column(String(300))
    data_hora = Column(DateTime, default=datetime.now)
