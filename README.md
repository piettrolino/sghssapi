SGHSS API - Sistema de Gestão Hospitalar e Saúde
Uma API RESTful completa e modular desenvolvida com FastAPI para o gerenciamento de processos hospitalares e de saúde. O sistema abrange a gestão de pacientes, medicos, agendamento de consultas, leitos e prontuários eletrônicos, contando com autenticação segura via JSON Web Tokens (JWT).

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.10+

Framework: FastAPI

ORM: SQLAlchemy

Validação de Dados: Pydantic V2

Banco de Dados: PostgreSQL

Autenticação: JWT (JSON Web Tokens) & Passlib (Bcrypt)

Gerenciamento de Dependências: PIP / venv

📐 Arquitetura do Projeto
O projeto segue uma estrutura modular focada em separação de responsabilidades (Clean Code):

Plaintext
sghss_api/
│
├── app/
│   ├── database.py       # Configuração da conexão com o banco de dados
│   ├── main.py           # Ponto de entrada da aplicação FastAPI
│   ├── security.py       # Hashing de senhas e geração/validação de JWT
│   │
│   ├── models/           # Mapeamento das tabelas do banco (SQLAlchemy)
│   │   ├── doctor_model.py
│   │   ├── patient_model.py
│   │   └── consulta_model.py
│   │
│   ├── schemas/          # Schemas de validação de dados (Pydantic V2)
│   │   ├── doctor_schema.py
│   │   ├── patient_schema.py
│   │   └── consulta_schema.py
│   │
│   └── routers/          # Endpoints da API
│       ├── doctor_router.py
│       ├── patient_router.py
│       └── consulta_router.py
│
├── .env.example          # Exemplo de variáveis de ambiente
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do repositório
🚀 Como Executar o Projeto Localmente
Pré-requisitos
Python 3.10 ou superior instalado.

Instância do PostgreSQL rodando (localmente ou via Docker).

Passo a Passo
Clonar o repositório:

Bash
git clone https://github.com/seu-usuario/sghss-api.git
cd sghss-api
Criar e ativar o ambiente virtual:

Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
Instalar as dependências:

Bash
pip install -r requirements.txt
Configurar as Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto com base no arquivo .env.example:

Snippet de código
DATABASE_URL=postgresql://usuario:senha@localhost:5432/sghss_db
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Executar a aplicação:

Bash
uvicorn app.main:app --reload
A API estará acessível em [http://127.0.2.1:8000](http://127.0.2.1:8000).

📑 Documentação Interativa (Swagger / Redoc)
O FastAPI gera automaticamente a documentação das rotas. Com a aplicação rodando, você pode acessar:

Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

🔒 Endpoints e Funcionalidades Principais
Médicos (/doctors): Cadastro, listagem e busca por CRM/Especialidade.

Pacientes (/patients): Gestão completa dos dados cadastrais dos pacientes.

Consultas (/consultas): Agendamento e histórico de consultas médicas.

Autenticação (/auth): Login e geração de token de acesso JWT para proteção das rotas.
