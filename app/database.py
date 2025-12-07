from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🚨 Configuração do PostgreSQL 🚨
# Altere 'SUA_SENHA_POSTGRES' para a senha que você definiu na instalação.
# O padrão é que o usuário seja 'postgres' e a porta seja 5432.
# Certifique-se que o banco de dados 'sghss' existe no PostgreSQL.
DATABASE_URL = "postgresql+psycopg://postgres:root@localhost:5432/sghss"

# O 'pool_pre_ping' ajuda a manter as conexões ativas e evitar erros de time-out
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declaração dos modelos
Base = declarative_base()

# Dependência para uso nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()