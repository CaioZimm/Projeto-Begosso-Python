class Autor:
    def __init__(self, codigo, nome, cod_cidade):
        self.codigo = codigo
        self.nome = nome
        self.cod_cidade = cod_cidade

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __repr__(self):
        return f"{self.codigo} - {self.nome} (Cidade: {self.cod_cidade})"
