from cursos.controller import CursoController
from utils.ui import limpar_tela

def menu_cursos(cursos_db):
    controller = CursoController(cursos_db)

    while True:
        limpar_tela()
        print("\n==== Menu Cursos ====\n")
        print("1 - Adicionar Curso")
        print("2 - Listar Cursos")
        print("3 - Buscar Curso")
        print("4 - Remover Curso")
        print("0 - Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            controller.adicionar_curso()
        elif opcao == "2":
            controller.listar_cursos()
        elif opcao == "3":
            controller.buscar_curso()
        elif opcao == "4":
            controller.remover_curso()

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")