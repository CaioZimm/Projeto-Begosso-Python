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
            descricao = input("Descrição: ")
            estado = input("Estado (UF): ")
            sucesso, msg = controller.adicionar_cidade(descricao, estado)
            print(msg)

        elif opcao == "2":
            cidades = controller.listar_cidades()
            if not cidades:
                print("Nenhuma cidade cadastrada.")
            for cidade in cidades:
                print(cidade)

        elif opcao == "3":
            codigo = int(input("Código da cidade: "))
            cidade = controller.buscar_cidade(codigo)
            print(cidade if cidade else "Cidade não encontrada.")

        elif opcao == "4":
            codigo = int(input("Código da cidade: "))
            sucesso, msg = controller.remover_cidade(codigo)
            print(msg)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")