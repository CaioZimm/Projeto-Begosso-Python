from livros.repository import LivrosDB
from livros.controller import LivroController
from utils.ui import limpar_tela

db = LivrosDB()
controller = LivroController(db)

def menu_livros():
    while True:
        limpar_tela()
        print("\n--- Menu Livros ---\n")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Remover Livro")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            controller.adicionar_livro()
        elif opcao == "2":
            controller.listar_livros()
        elif opcao == "3":
            controller.buscar_livro()
        elif opcao == "4":
            controller.remover_livro()

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            
        input("\nPressione Enter para continuar...")
