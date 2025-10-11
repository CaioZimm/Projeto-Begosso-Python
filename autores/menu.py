from autores.controller import AutorController
from utils.ui import limpar_tela

controller = AutorController()

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
            controller.adicionar_autor()
        elif opcao == "2":
            controller.listar_autores()
        elif opcao == "3":
            controller.buscar_autor()
        elif opcao == "4":
            controller.remover_autor()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")