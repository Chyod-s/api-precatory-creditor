# Precatory Management System

Este projeto é uma API com frontend integrado para gerenciamento de precatórios, credores, certidões e documentos pessoais. Desenvolvido com **Python**, **Flask**, **SQLAlchemy**, **JWT**, **Tailwind CSS** com **Alembic** para versionamento e arquitetura baseada em **Clean Architecture**.

---

### Interface do sistema

[Veja as imagens do frontend aqui](https://github.com/Chyod-s/api-precatory-creditor/tree/main/src/api_main/static/assets/fotos_front)


## Tecnologias Utilizadas

- **Backend:** Python, Flask, SQLAlchemy, Alembic
- **Frontend:** Jinja2, Tailwind CSS, JavaScript
- **Autenticação:** JWT
- **Banco de Dados:** SQLite (desenvolvimento), com suporte para outros via SQLAlchemy
- **Task Scheduler:** Agendador customizado com execução via scripts
- **Containerização:** Docker + Docker Compose
- **Test:** Pytest

---

## Autenticação

O projeto utiliza **JWT** para autenticação de usuários. As rotas protegidas exigem envio de token no cabeçalho `Authorization`.

---
Configuração e Execução (Docker)

### Pré-requisitos
- [Docker `download`](https://www.docker.com/get-started/)

### Instalação manual

1 - Suba os containers com build forçado:
```bash
docker-compose up -d --build
```
2 - Acesse a aplicação:
```bash
http://localhost:5055
```
---

Configuração e Execução (Desenvolvimento)

### Pré-requisitos

- Python 3.10+
- Docker & Docker Compose (opcional)
- Node.js (para Tailwind)

### Instalação manual

```bash
# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate # no linux  
.venv\Scripts\Activate.ps1 # no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
alembic upgrade head

# Inicie a aplicação
python src/api_main/main.py # api principal
python src/api_main/main.py # api mockada
```

## Funcionalidades

- [x] Cadastro e login de usuários

- [x] Registro de credores

- [x] Cadastro de certidões e documentos pessoais

- [x] Consulta de precatórios

- [x] Integração com Swagger para documentação

- [x] Frontend responsivo com Tailwind

- [x] Execução de tarefas automáticas via agendador


## Decisões técnicas e raciocínio

Montei o projeto separando bem as responsabilidades pra facilitar manutenção e leitura do código. Escolhi Flask por ser leve e direto, SQLAlchemy pra ter mais flexibilidade com o banco, e JWT pra autenticação. No frontend usei Jinja2 com Tailwind, que funcionam bem junto com Flask. Também incluí um agendador simples pra simular execuções automáticas. Deixei tudo pronto pra rodar com Docker ou direto no Python.

Utilizei:

- **Flask** pela sua leveza e flexibilidade.

- **SQLAlchemy** para facilitar a portabilidade entre bancos de dados.

- **Alembic** para controle de versão do schema do banco.

- **JWT** para autenticação segura e stateless.

- **Jinja2 + Tailwind CSS** no frontend por serem simples e diretos, além de estarem integrados ao Flask.

- Um **agendador customizado** foi implementado para simular tarefas automáticas, sem depender de bibliotecas externas pesadas.

Também organizei a estrutura pensando em facilitar os testes e a integração com outros ambientes. Usei pytest nos testes e deixei o projeto pronto pra rodar com Docker, o que ajuda na instalação e evita problemas com dependências.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
