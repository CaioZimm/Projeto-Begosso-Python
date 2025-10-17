from datetime import datetime
from emprestimos.model import Emprestimo

class EmprestimoService:
    def __init__(self, emprestimos_db, livros_db, alunos_db):
        self.db = emprestimos_db
        self.livros_db = livros_db
        self.alunos_db = alunos_db

    def realizar_emprestimo(self, cod_livro, cod_aluno):
        livro = self.livros_db.buscar_livro(cod_livro)
        aluno = self.alunos_db.buscar_aluno(cod_aluno)

        if not livro:
            return False, "Livro não encontrado."
        if not aluno:
            return False, "Aluno não encontrado."

        if livro.disponibilidade.lower() != "disponível":
            return False, f"O livro '{livro.titulo}' já está emprestado."

        codigo = self.db.novo_codigo()
        emprestimo = Emprestimo(codigo, cod_livro, cod_aluno)
        self.db.adicionar_emprestimo(emprestimo)

        livro.disponibilidade = "emprestado"
        self.livros_db.salvar_livros()

        return True, f"Empréstimo registrado! Código: {codigo} - Devolução até {emprestimo.data_devolucao}"

    def devolver_livro(self, cod_emprestimo):
        emp = self.db.buscar_emprestimo(cod_emprestimo)
        if not emp:
            return False, "Empréstimo não encontrado."

        livro = self.livros_db.buscar_livro(emp.cod_livro)
        if not livro:
            return False, "Livro não encontrado."

        if emp.devolvido.lower() == "sim":
            return False, "Esse livro já foi devolvido."

        hoje = datetime.today().date()
        data_dev = datetime.strptime(emp.data_devolucao, "%d/%m/%Y").date()
        atrasado = hoje > data_dev

        emp.devolvido = "Sim"
        livro.disponibilidade = "disponível"
        self.livros_db.salvar_livros()
        self.db.salvar_emprestimos()

        if atrasado:
            return True, "Livro devolvido, mas estava atrasado!"
        return True, "Devolução realizada com sucesso!"

    def listar_emprestimos_completo(self):
        resultado = []
        livros = self.livros_db
        alunos = self.alunos_db
        for e in self.db.listar_emprestimos():
            livro = livros.buscar_livro(e.cod_livro)
            aluno = alunos.buscar_aluno(e.cod_aluno)
            resultado.append(
                f"{e.codigo} - {livro.titulo if livro else 'Livro?'} / {aluno.nome if aluno else 'Aluno?'}\n"
                f"   Empréstimo: {e.data_emprestimo} | Devolução: {e.data_devolucao}\n"
                f"   Devolvido: {e.devolvido}"
            )
        return resultado

    def listar_livros_emprestados(self):
        return [e for e in self.db.listar_emprestimos() if e.devolvido.lower() != "sim"]

    def listar_atrasados(self):
        hoje = datetime.today().date()
        atrasados = []
        for e in self.db.listar_emprestimos():
            data_dev = datetime.strptime(e.data_devolucao, "%d/%m/%Y").date()
            if hoje > data_dev and e.devolvido.lower() != "sim":
                atrasados.append(e)
        return atrasados