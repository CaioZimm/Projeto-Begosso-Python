from emprestimos.service import EmprestimoService

class EmprestimoController:
    def __init__(self, emprestimos_db, livros_db, alunos_db):
        self.service = EmprestimoService(emprestimos_db, livros_db, alunos_db)
        self.livros_db = livros_db
        self.alunos_db = alunos_db

    def realizar_emprestimo(self):
        livros = self.livros_db.listar_livros()
        alunos = self.alunos_db.listar_alunos()

        if not livros or not alunos:
            print("É necessário ter pelo menos um livro e um aluno cadastrados!")
            return

        try:
            print("\n--- Livros Disponíveis ---")
            for l in livros:
                if l.disponibilidade.lower() == "disponível":
                    print(f"{l.codigo} - {l.titulo}")

            print("\n--- Alunos ---")
            for a in alunos:
                print(f"{a.codigo} - {a.nome}")

            cod_livro = int(input("\nCódigo do livro: "))
            cod_aluno = int(input("Código do aluno: "))

            sucesso, msg = self.service.realizar_emprestimo(cod_livro, cod_aluno)
            print(msg)

        except ValueError:
            print("Código inválido.")

    def devolver_livro(self):
        try:
            cod_emp = int(input("Código do empréstimo para devolver: "))
            sucesso, msg = self.service.devolver_livro(cod_emp)
            print(msg)
        except ValueError:
            print("Código inválido.")

    def listar_emprestimos(self):
        emprestimos = self.service.listar_emprestimos_completo()
        if not emprestimos:
            print("Nenhum empréstimo cadastrado.")
        else:
            for e in emprestimos:
                print(e)
                print("-" * 50)

    def listar_atrasados(self):
        atrasados = self.service.listar_atrasados()
        if not atrasados:
            print("Nenhum livro atrasado.")
        else:
            for e in atrasados:
                print(e)
                print("-" * 40)
