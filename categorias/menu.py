from categorias.repository import CategoriasDB
from categorias.controller import CategoriaController
from utils.ui import limpar_tela

db = CategoriasDB()
controller = CategoriaController(db)

def menu_categorias():
    while True:
        limpar_tela()
        print("\n--- Menu Categorias ---\n")
        print("1. Adicionar Categoria")
        print("2. Listar Categorias")
        print("3. Buscar Categoria")
        print("4. Remover Categoria")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            descricao = input("Descrição da categoria: ").strip()
            sucesso, msg = controller.adicionar_categoria(descricao)
            print(msg)
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            categorias = controller.listar_categorias()
            if not categorias:
                print("Nenhuma categoria cadastrada.")
            else:
                for c in categorias:
                    print(c)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            try:
                codigo = int(input("Código da categoria: "))
                categoria = controller.buscar_categoria(codigo)
                print(categoria if categoria else "Categoria não encontrada.")
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            try:
                codigo = int(input("Código da categoria: "))
                sucesso, msg = controller.remover_categoria(codigo)
                print(msg)
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")