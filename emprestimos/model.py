from datetime import date, timedelta

class Emprestimo:
    def __init__(self, codigo: int, cod_livro: int, cod_aluno: int, data_emprestimo: str = None, data_devolucao: str = None, devolvido: str = "Não"):
        self.codigo = codigo
        self.cod_livro = cod_livro
        self.cod_aluno = cod_aluno
        self.data_emprestimo = data_emprestimo or date.today().strftime("%d/%m/%Y")
        self.data_devolucao = data_devolucao or (date.today() + timedelta(days=7)).strftime("%d/%m/%Y")
        self.devolvido = devolvido

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __repr__(self):
        return f"{self.codigo} - Livro {self.cod_livro} / Aluno {self.cod_aluno} | {self.data_emprestimo} → {self.data_devolucao} | Devolvido: {self.devolvido}"
