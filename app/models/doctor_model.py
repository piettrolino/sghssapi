from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # <-- Importação adicionada
from app.database import Base


class Doctor(Base):
    # O nome da tabela deve ser igual ao referenciado nas Foreign Keys
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    crm = Column(String(50), unique=True, nullable=False)
    specialty = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)

    # RELACIONAMENTOS BIDIRECIONAIS

    # 1. Relacionamento com Prontuario: Prontuários atendidos por este profissional
    # 'prontuarios_atendidos' corresponde ao back_populates em Prontuario
    prontuarios_atendidos = relationship("Prontuario", back_populates="profissional")

    # 2. Relacionamento com Consulta: Consultas agendadas com este profissional
    # 'consultas_agendadas' corresponde ao back_populates em Consulta
    consultas_agendadas = relationship("Consulta", back_populates="profissional")