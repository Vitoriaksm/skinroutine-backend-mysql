# ==============================================================================
# MÓDULO DE CONEXÃO COM O BANCO DE DADOS (ITEM 1)
# ==============================================================================
import mysql.connector
from mysql.connector import Error, errorcode

def criar_conexao():
    """Estabelece a conexão com o MySQL e trata falhas de infraestrutura."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          # Altere para seu usuário do MySQL local
            password="sua_senha",  # Altere para sua senha do MySQL local
            database="skincare_db",
            port=3306
        )
        if conexao.is_connected():
            return conexao

    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("\n [ERRO DE CONEXÃO] Usuário ou senha do MySQL estão incorretos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("\n [ERRO DE CONEXÃO] O banco 'skincare_db' não existe. Execute o script .sql da Entrega 4.")
        elif err.errno == 2003:
            print("\n [ERRO DE CONEXÃO] O servidor MySQL está offline. Ligue o MySQL na sua máquina.")
        else:
            print(f"\n [ERRO DE CONEXÃO] Falha inesperada: {err}")
        return None
