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
