from livros.service import LivroService

class LivroController:
    def __init__(self, db):
        self.service = LivroService(db)

    def adicionar_livro(self, titulo, cod_autor, cod_categoria, ano_publicacao):
        return self.service.adicionar_livro(titulo, cod_autor, cod_categoria, ano_publicacao)

    def listar_livros(self):
        return self.service.listar_livros_completo()

    def buscar_livro(self, codigo):
        return self.service.buscar_livro_completo(codigo)

    def remover_livro(self, codigo):
        return self.service.remover_livro(codigo)
