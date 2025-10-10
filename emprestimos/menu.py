from emprestimos.repository import EmprestimosDB
from emprestimos.controller import EmprestimoController
from livros.repository import LivrosDB
from alunos.repository import AlunosDB
from utils.ui import limpar_tela

db = EmprestimosDB()
controller = EmprestimoController(db)
livros_db = LivrosDB()
alunos_db = AlunosDB()

def menu_emprestimos():
    while True:
        limpar_tela()
        print("\n--- Menu Empréstimos ---\n")
        print("1. Realizar Empréstimo")
        print("2. Registrar Devolução")
        print("3. Listar Empréstimos")
        print("4. Listar Livros Atrasados")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            livros = livros_db.listar_livros()
            alunos = alunos_db.listar_alunos()

            if not livros or not alunos:
                print("Precisa cadastrar livros e alunos primeiro!")
                input("\nPressione Enter para continuar...")
                continue

            print("\n--- Livros Disponíveis ---")
            for l in livros:
                if l.disponibilidade.lower() == "disponível":
                    print(f"{l.codigo} - {l.titulo}")

            print("\n--- Alunos ---")
            for a in alunos:
                print(f"{a.codigo} - {a.nome}")

            try:
                cod_livro = int(input("\nCódigo do livro: "))
                cod_aluno = int(input("Código do aluno: "))
                sucesso, msg = controller.realizar_emprestimo(cod_livro, cod_aluno)
                print(msg)
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            emprestimos = controller.listar_emprestimos()
            if not emprestimos:
                print("Nenhum empréstimo registrado.")
            else:
                print("\n--- Empréstimos Ativos ---")
                for e in emprestimos:
                    print(e)
                    print("-" * 40)
            try:
                cod_emp = int(input("Código do empréstimo para devolver: "))
                sucesso, msg = controller.devolver_livro(cod_emp)
                print(msg)
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            emprestimos = controller.listar_emprestimos()
            if not emprestimos:
                print("Nenhum empréstimo cadastrado.")
            else:
                for e in emprestimos:
                    print(e)
                    print("-" * 50)
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            atrasados = controller.listar_atrasados()
            if not atrasados:
                print("Nenhum livro atrasado.")
            else:
                for e in atrasados:
                    print(e)
                    print("-" * 40)
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")
