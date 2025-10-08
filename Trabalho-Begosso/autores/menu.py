from autores.repository import AutoresDB
from autores.controller import AutorController
from cidades.repository import CidadesDB
from utils.ui import limpar_tela

db = AutoresDB()
controller = AutorController(db)
cidades_db = CidadesDB()

def menu_autores():
    while True:
        limpar_tela()
        print("\n--- Menu Autores ---\n")
        print("1. Adicionar Autor")
        print("2. Listar Autores")
        print("3. Buscar Autor")
        print("4. Remover Autor")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cidades = cidades_db.listar_cidades()

            if not cidades:
                print("Precisa cadastrar uma cidade primeiro!")
                input("\nPressione Enter para continuar...")
                continue

            print("\n--- Cidades Disponíveis ---")
            for c in cidades:
                print(f"{c.codigo} - {c.descricao} ({c.estado})")

            try:
                nome = input("\nNome do autor: ").strip()
                cod_cidade = int(input("Código da cidade: "))
                sucesso, msg = controller.adicionar_autor(nome, cod_cidade)
                print(msg)
            except ValueError:
                print("Código inválido! Retornando ao menu.")
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            autores = controller.listar_autores()
            if not autores:
                print("Nenhum autor cadastrado.")
            else:
                for a in autores:
                    print(a)
                    print("-" * 40)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            try:
                codigo = int(input("Código do autor: "))
                autor = controller.buscar_autor(codigo)
                print(autor if autor else "Autor não encontrado.")
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            try:
                codigo = int(input("Código do autor: "))
                sucesso, msg = controller.remover_autor(codigo)
                print(msg)
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")
