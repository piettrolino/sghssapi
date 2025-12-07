from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from app.database import Base

class Internacao(Base):
    __tablename__ = "internacoes"

    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    leito_id = Column(Integer, ForeignKey("leitos.id"), nullable=False)
    data_entrada = Column(DateTime, default=datetime.now)
    data_alta = Column(DateTime, nullable=True)
