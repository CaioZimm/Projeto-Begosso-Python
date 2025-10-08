from cursos.repository import CursosDB
from cursos.controller import CursoController

db_cursos = CursosDB()
controller = CursoController(db_cursos)

def menu_cursos():
    while True:
        print("\n--- Menu Cursos ---")
        print("1. Adicionar Curso")
        print("2. Listar Cursos")
        print("3. Buscar Curso")
        print("4. Remover Curso")
        print("0. Voltar")
        escolha = input("Escolha: ").strip()

        if escolha == '1':
            cod = input("Código: ").strip()
            nome = input("Nome: ").strip()
            sucesso, msg = controller.adicionar_curso(cod, nome)
            print(msg)
        elif escolha == '2':
            cursos = controller.listar_cursos()
            if cursos:
                for c in cursos:
                    print(c)
            else:
                print("Nenhum curso cadastrado.")
        elif escolha == '3':
            cod = input("Código: ").strip()
            c = controller.buscar_curso(cod)
            print(f"Encontrado: {c}" if c else "Curso não encontrado.")
        elif escolha == '4':
            cod = input("Código: ").strip()
            print("Curso removido!" if controller.remover_curso(cod) else "Curso não encontrado.")
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")
