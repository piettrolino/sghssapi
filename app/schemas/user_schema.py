from pydantic import BaseModel, Field


# 1. SCHEMA DE INPUT (O que o usuário envia no POST /register)
# Contém as regras de validação para a senha de texto simples (72 chars)
class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str = Field(..., min_length=8, max_length=72)
    perfil: str


# 2. SCHEMA DE OUTPUT (O que a API retorna após o registro)
# Este schema NÃO inclui a senha/hash, eliminando o erro.
class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str

    # Configuração para o Pydantic entender os objetos do SQLAlchemy
    class Config:
        from_attributes = True
        # ou orm_mode = True, se você estiver em uma versão mais antiga do Pydantic.