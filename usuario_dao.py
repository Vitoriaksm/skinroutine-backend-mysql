# ==============================================================================
# CAMADA DAO (DATA ACCESS OBJECT - ITEM 2 & 3)
# ==============================================================================
from conexao import criar_conexao
from mysql.connector import Error

class UsuarioDAO:

    # --- CREATE (INSERIR) ---
    def inserir(self, nome, email, senha, tipo_pele):
        conn = criar_conexao()
        if not conn:
            return

        cursor = conn.cursor()
        try:
            tipo_pele_valido = tipo_pele.upper() if tipo_pele else None
            sql = """
                INSERT INTO usuarios (nome, email, senha_hash, tipo_pele) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nome, email, senha, tipo_pele_valido))
            conn.commit()
            print(f"\n[SUCESSO] Usuário '{nome}' cadastrado com sucesso! (ID Gerado: {cursor.lastrowid})")
        except Error as e:
            conn.rollback()
            print(f"\n[ERRO SQL] Falha ao cadastrar usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    # --- READ (LISTAR TODOS) ---
    def listar_usuarios(self):
        conn = criar_conexao()
        if not conn:
            return

        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_usuario, nome, email, tipo_pele, data_cadastro FROM usuarios"
            cursor.execute(sql)
            usuarios = cursor.fetchall()

            print("\n--- LISTA DE USUÁRIOS (SKINCARE_DB) ---")
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for u in usuarios:
                    print(f"ID: {u['id_usuario']} | Nome: {u['nome']} | Email: {u['email']} | Tipo: {u['tipo_pele']}")
        except Error as e:
            print(f"\n[ERRO SQL] Falha ao consultar usuários: {e}")
        finally:
            cursor.close()
            conn.close()

    # --- READ ESPECÍFICO (BUSCAR POR ID) ---
    def buscar_por_id(self, id_usuario):
        conn = criar_conexao()
        if not conn:
            return

        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_usuario, nome, email, tipo_pele, data_cadastro FROM usuarios WHERE id_usuario = %s"
            cursor.execute(sql, (id_usuario,))
            usuario = cursor.fetchone()

            if usuario:
                print(f"\n--- USUÁRIO LOCALIZADO ---")
                print(f"ID: {usuario['id_usuario']}\nNome: {usuario['nome']}\nEmail: {usuario['email']}\nTipo de Pele: {usuario['tipo_pele']}")
            else:
                print(f"\n[AVISO] Nenhum usuário encontrado com o ID {id_usuario}.")
        except Error as e:
            print(f"\n[ERRO SQL] Falha ao buscar por ID: {e}")
        finally:
            cursor.close()
            conn.close()

    # --- UPDATE (ATUALIZAR) ---
    def atualizar(self, id_usuario, novo_nome):
        conn = criar_conexao()
        if not conn:
            return

        cursor = conn.cursor()
        try:
            sql = "UPDATE usuarios SET nome = %s WHERE id_usuario = %s"
            cursor.execute(sql, (novo_nome, id_usuario))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Usuário ID {id_usuario} atualizado com sucesso!")
            else:
                print(f"\n[AVISO] Nenhum usuário localizado com o ID {id_usuario}.")
        except Error as e:
            conn.rollback()
            print(f"\n[ERRO SQL] Falha ao atualizar usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    # --- DELETE (DELETAR) ---
    def deletar(self, id_usuario):
        conn = criar_conexao()
        if not conn:
            return

        cursor = conn.cursor()
        try:
            sql = "DELETE FROM usuarios WHERE id_usuario = %s"
            cursor.execute(sql, (id_usuario,))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Usuário ID {id_usuario} deletado com sucesso do banco!")
            else:
                print(f"\n[AVISO] Nenhum usuário localizado com o ID {id_usuario}.")
        except Error as e:
            conn.rollback()
            print(f"\n[ERRO SQL] Falha ao deletar usuário: {e}")
        finally:
            cursor.close()
            conn.close()
            conn.close()
