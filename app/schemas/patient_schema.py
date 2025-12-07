# app/schemas/patient_schema.py

from pydantic import BaseModel, EmailStr


# ...

class PatientCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

class PatientResponse(PatientCreate):
    id: int
    # Adicione a configuração do ORM mode (ou from_attributes no Pydantic v2)
    # para permitir que ele leia do Model SQLAlchemy
    class Config:
        # Renomear de orm_mode para from_attributes, como seus warnings já indicavam
        from_attributes = True