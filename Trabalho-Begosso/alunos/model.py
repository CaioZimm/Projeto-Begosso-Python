class Aluno:
    def __init__(self, codigo, nome, codigocurso, codigocidade):
        self.codigo = codigo
        self.nome = nome
        self.codigocurso = codigocurso
        self.codigocidade = codigocidade

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __repr__(self):
        return f"{self.codigo} - {self.nome} | Curso: {self.codigocurso} | Cidade: {self.codigocidade}"