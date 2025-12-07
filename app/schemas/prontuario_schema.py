from pydantic import BaseModel
from datetime import datetime

class ProntuarioBase(BaseModel):
    paciente_id: int
    profissional_id: int
    descricao: str
    diagnostico: str
    prescricao: str

class ProntuarioCreate(ProntuarioBase):
    pass

class Prontuario(ProntuarioBase):
    id: int
    data_hora: datetime

    class Config:
        orm_mode = True
