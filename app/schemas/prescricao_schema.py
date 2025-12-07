from pydantic import BaseModel
from datetime import datetime

class PrescricaoBase(BaseModel):
    paciente_id: int
    medico_id: int
    texto: str

class PrescricaoCreate(PrescricaoBase):
    pass

class Prescricao(PrescricaoBase):
    id: int
    data: datetime

    class Config:
        orm_mode = True
