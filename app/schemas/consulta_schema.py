from pydantic import BaseModel
from datetime import datetime

class ConsultaBase(BaseModel):
    paciente_id: int
    profissional_id: int
    data_hora: datetime
    motivo: str | None = None
    status: str | None = "agendada"

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(BaseModel):
    data_hora: datetime | None = None
    motivo: str | None = None
    status: str | None = None

class ConsultaOut(ConsultaBase):
    id: int

    class Config:
        orm_mode = True
