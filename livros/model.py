class Livro:
    def __init__(self, codigo, titulo, cod_autor, cod_categoria, ano_publicacao, disponibilidade: str = "disponível"):
        self.codigo = codigo
        self.titulo = titulo
        self.cod_autor = cod_autor
        self.cod_categoria = cod_categoria
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade

    def __lt__(self, other):
        return self.codigo < other.codigo

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __repr__(self):
        return f"{self.codigo} - {self.titulo} ({self.ano_publicacao}) [{self.disponibilidade}]"
