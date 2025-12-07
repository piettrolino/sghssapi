from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(200), nullable=False)
    perfil = Column(String(50), nullable=False)  # paciente / medico / admin
