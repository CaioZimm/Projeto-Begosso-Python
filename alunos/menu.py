from alunos.controller import AlunoController
from utils.ui import limpar_tela

def menu_alunos(alunos_db, cursos_db, cidades_db):
    controller = AlunoController(alunos_db, cursos_db, cidades_db)

    while True:
        limpar_tela()
        print("\n==== Menu Alunos ====\n")
        print("1 - Adicionar Aluno")
        print("2 - Listar Alunos")
        print("3 - Buscar Aluno")
        print("4 - Remover Aluno")
        print("0 - Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            controller.adicionar_aluno()
        elif opcao == "2":
            controller.listar_alunos()
        elif opcao == "3":
            controller.buscar_aluno()
        elif opcao == "4":
            controller.remover_aluno()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")