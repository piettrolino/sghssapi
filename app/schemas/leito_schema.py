from pydantic import BaseModel, Field
from typing import Optional


# SCHEMA DE INPUT (Para criar ou atualizar um leito)
# Define o que o usuário deve enviar na requisição POST.
class LeitoCreate(BaseModel):
    # O tipo é obrigatório e limitado a 50 caracteres (para evitar erros no BD)
    tipo: str = Field(..., max_length=50, description="Tipo de leito: enfermaria, UTI, isolamento")

    # O status deve ser um dos valores definidos e tem um valor padrão
    status: str = Field("Livre", max_length=20, description="Status do leito: Livre ou Ocupado")


# SCHEMA DE OUTPUT (Para listar ou retornar um leito)
# Adiciona o 'id' gerado pelo banco de dados ao retornar o objeto.
class Leito(LeitoCreate):
    id: int

    # Configuração obrigatória para que o Pydantic leia dados do SQLAlchemy
    class Config:
        from_attributes = True
        # Se você estiver usando uma versão mais antiga do Pydantic, use:
        # orm_mode = True
