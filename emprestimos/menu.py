from emprestimos.controller import EmprestimoController
from utils.ui import limpar_tela

def menu_emprestimos(emprestimos_db, livros_db, alunos_db):
    controller = EmprestimoController(emprestimos_db, livros_db, alunos_db)

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
            controller.realizar_emprestimo()
        elif opcao == "2":
            controller.devolver_livro()
        elif opcao == "3":
            controller.listar_emprestimos()
        elif opcao == "4":
            controller.listar_atrasados()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
        
        input("\nPressione Enter para continuar...")
