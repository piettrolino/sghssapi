# app/schemas/leito_schema.py

from pydantic import BaseModel, Field
from typing import Optional


# INPUT: O que o administrador envia para criar um leito
class LeitoCreate(BaseModel):
    tipo: str = Field(..., max_length=50, description="Tipo de leito: enfermaria, UTI, isolamento")
    status: str = Field("Livre", max_length=20, description="Status inicial do leito: Livre ou Ocupado")


# OUTPUT: O que a API retorna
class Leito(LeitoCreate):
    id: int

    class Config:
        from_attributes = True
        # ou orm_mode = True, dependendo da sua versão Pydantic.