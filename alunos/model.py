class Aluno:
    def __init__(self, codigo, nome, cod_curso, cod_cidade):
        self.codigo = codigo
        self.nome = nome
        self.cod_curso = cod_curso
        self.cod_cidade = cod_cidade

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __repr__(self):
        return f"{self.codigo} - {self.nome} (Curso: {self.cod_curso}, Cidade: {self.cod_cidade})"
