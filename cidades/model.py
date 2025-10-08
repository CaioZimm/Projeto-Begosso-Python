class Cidade:
    def __init__(self, codigo, descricao, estado):
        self.codigo = codigo
        self.descricao = descricao
        self.estado = estado

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __repr__(self):
        return f"{self.codigo} - {self.descricao} ({self.estado})"