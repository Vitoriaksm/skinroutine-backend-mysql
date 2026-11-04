# ==============================================================================
# MENU PRINCIPAL (INTERFACE DO USUÁRIO)
# ==============================================================================
from usuario_dao import UsuarioDAO

def main():
    dao = UsuarioDAO()

    while True:
        print("\n=== SISTEMA SKINROUTINE (PYTHON DAO) ===")
        print("1. Cadastrar Usuario (Create)")
        print("2. Listar Todos os Usuarios (Read)")
        print("3. Buscar Usuario por ID (Read Especifico)")
        print("4. Atualizar Usuario (Update)")
        print("5. Deletar Usuario (Delete)")
        print("0. Sair")
        
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == '1':
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            senha = input("Senha: ").strip()
            tipo_pele = input("Tipo de Pele (SECA, OLEOSA, MISTA, NORMAL, SENSIVEL): ").strip()
            
            if not nome or not email or not senha:
                print("\n[ERRO] Nome, E-mail e Senha sao obrigatorios!")
            else:
                dao.inserir(nome, email, senha, tipo_pele)
            
        elif opcao == '2':
            dao.listar_usuarios()
            
        elif opcao == '3':
            id_usuario = input("Digite o ID do usuario que deseja buscar: ").strip()
            if id_usuario.isdigit():
                dao.buscar_por_id(int(id_usuario))
            else:
                print("\n[ERRO] Digite um ID numérico valido!")
            
        elif opcao == '4':
            id_usuario = input("ID do usuario que deseja atualizar: ").strip()
            if id_usuario.isdigit():
                novo_nome = input("Novo nome: ").strip()
                if novo_nome:
                    dao.atualizar(int(id_usuario), novo_nome)
                else:
                    print("\n[ERRO] O novo nome nao pode ser vazio!")
            else:
                print("\n[ERRO] Digite um ID numérico valido!")
            
        elif opcao == '5':
            id_usuario = input("ID do usuario que deseja deletar: ").strip()
            if id_usuario.isdigit():
                dao.deletar(int(id_usuario))
            else:
                print("\n[ERRO] Digite um ID numérico valido!")
            
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opcao invalida!")

if __name__ == "__main__":
    main()
