from fastapi import FastAPI
from app.database import engine, Base

# Importando o objeto 'router' de cada módulo
from app.routers.patient_router import router as patient_router
from app.routers.doctor_router import router as doctor_router
from app.routers.consulta_router import router as consulta_router
from app.routers.prontuario_router import router as prontuario_router
from app.routers.auth_router import router as auth_router
from app.routers.leito_router import router as leito_router # <--- ADIÇÃO 1: Importa a rota Leito

# 🚨 IMPORTAÇÃO DOS MODELS PARA GARANTIR A CRIAÇÃO DE TODAS AS TABELAS
# O SQLAlchemy precisa "conhecer" todas as classes que herdam de Base
# antes de executar create_all.
import app.models.patient_model
import app.models.doctor_model
import app.models.user_model
import app.models.leito_model # <--- ADIÇÃO 2: Importa o Modelo Leito (Cria a Tabela)
# Adicione outros models (consulta, prontuario, etc.) se não estiverem sendo
# importados em patient_model ou doctor_model.

# 🚨 CRIAÇÃO DE TABELAS
# Esta linha cria todas as tabelas (pacientes, doctors, usuarios, leitos, etc.)
# no PostgreSQL mapeadas pelos seus Models Python.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SGHSS API")

# 1. Rotas de Recurso (com prefixo e tags para organização)
app.include_router(
    patient_router,
    prefix="/patients",
    tags=["Pacientes"]
)
app.include_router(
    doctor_router,
    prefix="/doctors",
    tags=["Profissionais"]
)
app.include_router(
    consulta_router,
    prefix="/consultas",
    tags=["Consultas"]
)
app.include_router(
    prontuario_router,
    prefix="/prontuarios",
    tags=["Prontuários"]
)
app.include_router( # <--- ADIÇÃO 3: Inclui o Roteador Leito na Aplicação
    leito_router,
    prefix="/leitos",
    tags=["Leitos"]
)

# 2. Rota de Autenticação
app.include_router(auth_router)