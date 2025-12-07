from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    crm: str
    specialty: str
    phone: str | None = None

class DoctorCreate(DoctorBase):
    pass

class DoctorResponse(DoctorBase):
    id: int

    class Config:
        orm_mode = True
