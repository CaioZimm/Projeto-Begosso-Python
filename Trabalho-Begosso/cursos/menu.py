from cursos.repository import CursosDB
from cursos.controller import CursoController

db = CursosDB()
controller = CursoController(db)

def menu_cursos():
    while True:
        print("\n--- Menu Cursos ---\n")
        print("1. Adicionar Curso")
        print("2. Listar Cursos")
        print("3. Buscar Curso")
        print("4. Remover Curso")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            descricao = input("Descrição do curso: ").strip()
            sucesso, msg = controller.adicionar_curso(descricao)
            print(msg)

        elif opcao == "2":
            cursos = controller.listar_cursos()
            if not cursos:
                print("Nenhum curso cadastrado.")
            for curso in cursos:
                print(curso)

        elif opcao == "3":
            try:
                codigo = int(input("Código do curso: "))
                curso = controller.buscar_curso(codigo)
                print(curso if curso else "Curso não encontrado.")
            except ValueError:
                print("Código inválido.")

        elif opcao == "4":
            try:
                codigo = int(input("Código do curso: "))
                sucesso, msg = controller.remover_curso(codigo)
                print(msg)
            except ValueError:
                print("Código inválido.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")