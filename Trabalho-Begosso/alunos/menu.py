from alunos.repository import AlunosDB
from alunos.controller import AlunoController
from cursos.repository import CursosDB
from cidades.repository import CidadesDB
from utils.ui import limpar_tela

db = AlunosDB()
controller = AlunoController(db)
cursos_db = CursosDB()
cidades_db = CidadesDB()

def menu_alunos():
    while True:
        limpar_tela()
        print("\n--- Menu Alunos ---\n")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Buscar Aluno")
        print("4. Remover Aluno")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cursos = cursos_db.listar_cursos()
            cidades = cidades_db.listar_cidades()

            if not cursos or not cidades:
                print("Precisa cadastrar uma cidade e um curso primeiro!")
                input("\nPressione Enter para continuar...")
                continue

            print("\n--- Cursos Disponíveis ---")
            for c in cursos:
                print(f"{c.codigo} - {c.descricao}")

            print("\n--- Cidades Disponíveis ---")
            for c in cidades:
                print(f"{c.codigo} - {c.descricao} ({c.estado})")

            try:
                nome = input("\nNome do aluno: ").strip()
                cod_curso = int(input("Código do curso: "))
                cod_cidade = int(input("Código da cidade: "))

                sucesso, msg = controller.adicionar_aluno(nome, cod_curso, cod_cidade)
                print(msg)
            except ValueError:
                print("Código inválido! Retornando ao menu.")
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            alunos = controller.listar_alunos()
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for a in alunos:
                    print(a)
                    print("-" * 40)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            try:
                codigo = int(input("Código do aluno: "))
                aluno = controller.buscar_aluno(codigo)
                print(aluno if aluno else "Aluno não encontrado.")
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            try:
                codigo = int(input("Código do aluno: "))
                sucesso, msg = controller.remover_aluno(codigo)
                print(msg)
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")
