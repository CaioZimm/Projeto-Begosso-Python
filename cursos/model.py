class Curso:
    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __repr__(self):
        return f"{self.codigo} - {self.descricao}"