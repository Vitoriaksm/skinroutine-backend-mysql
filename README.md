# 🧴 SkinRoutine — Sistema de Gerenciamento de Rotina de Skincare

Aplicação em **Python** integrada ao banco de dados **MySQL (`skincare_db`)**, desenvolvida para persistir e gerenciar informações de usuários e suas rotinas de cuidados com a pele. 

O projeto aplica o padrão de arquitetura **DAO (Data Access Object)** para isolar a lógica de acesso a dados da interface com o usuário, cobrindo o tratamento de exceções de conexão e as 4 operações fundamentais do CRUD.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem de Programação:** Python 3.x
- **Banco de Dados:** MySQL Server 8.x
- **Driver de Conexão:** `mysql-connector-python`
- **Padrões de Projeto:** Data Access Object (DAO) & Separação de Responsabilidades (CLI / DAO / Conexão)
- **Segurança:** Consultas SQL parametrizadas (`%s`) contra ataques de SQL Injection

---

## 📂 Arquitetura do Projeto

O código-fonte está estruturado de forma modular para garantir baixo acoplamento e reutilização:

```text
skincare-routine-system/
├── README.md               # Documentação completa do projeto
├── DDL_skincare_db.sql     # Script de criação do MySQL (Entrega 4)
├── conexao.py              # Camada de Conexão: Trata abertura e erros de infraestrutura
├── usuario_dao.py          # Camada DAO: Encapsula as operações do CRUD (SQL)
└── main.py                 # Camada de Apresentação: Interface interativa via terminal (CLI)
