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
            controller.adicionar_categoria()
        elif opcao == "2":
            controller.listar_categorias()
        elif opcao == "3":
            controller.buscar_categoria()
        elif opcao == "4":
            controller.remover_categoria()
            
        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")