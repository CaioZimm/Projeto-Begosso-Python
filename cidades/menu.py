from cidades.repository import CidadesDB
from cidades.controller import CidadeController
from utils.ui import limpar_tela

db = CidadesDB()
controller = CidadeController(db)

def menu_cidades():
    while True:
        limpar_tela()
        print("\n--- Menu Cidades ---\n")
        print("1. Adicionar Cidade")
        print("2. Listar Cidades")
        print("3. Buscar Cidade")
        print("4. Remover Cidade")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            controller.adicionar_cidade()
        elif opcao == "2":
            controller.listar_cidades()
        elif opcao == "3":
            controller.buscar_cidade()
        elif opcao == "4":
            controller.remover_cidade()
            
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")