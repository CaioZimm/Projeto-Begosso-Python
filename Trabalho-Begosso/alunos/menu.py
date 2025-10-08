from alunos.repository import AlunosDB
from alunos.controller import AlunoController

db_alunos = AlunosDB()
controller = AlunoController(db_alunos)

def menu_alunos():
    while True:
        print("\n--- Menu Alunos ---")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Buscar Aluno")
        print("4. Remover Aluno")
        print("0. Voltar\n")

        escolha = input("Escolha: ").strip()
        if escolha == '1':
            # Listar cursos

            codigo = print("Código: ")

            nome = input("Nome: ").strip()

            cursos = controller.listar_cursos()
            print("Cursos disponíveis:")
            for codigo, nome in cursos.items():
                print(f"{codigo}: {nome}")
            codigo_curso = input("Escolha o código do curso: ").strip()

            # Listar cidades
            cidades = controller.listar_cidades()
            print("Cidades disponíveis:")
            for codigo, nome in cidades.items():
                print(f"{codigo}: {nome}")
            codigo_cidade = input("Escolha o código da cidade: ").strip()

            # Adicionar aluno
            sucesso, msg = controller.adicionar_aluno(nome, codigo_curso, codigo_cidade)
            print(msg)

        elif escolha == '2':
            alunos = controller.listar_alunos()
            for a in alunos:
                print(a)

        elif escolha == '3':
            codigo = input("Código: ").strip()
            aluno = controller.buscar_aluno(codigo)
            print(aluno if aluno else "Aluno não encontrado.")

        elif escolha == '4':
            codigo = input("Código: ").strip()
            print("Removido!" if controller.remover_aluno(codigo) else "Aluno não encontrado.")

        elif escolha == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_alunos()
