from livros.service import LivroService

class LivroController:
    def __init__(self, livros_db, autores_db, categorias_db, cidades_db):
        self.service = LivroService(livros_db, autores_db, categorias_db, cidades_db)
        self.livros_db = livros_db
        self.autores_db = autores_db
        self.categorias_db = categorias_db
        self.cidades_db = cidades_db

    def adicionar_livro(self):
        autores = self.autores_db.listar_autores()
        categorias = self.categorias_db.listar_categorias()

        if not autores or not categorias:
            print("É necessário cadastrar pelo menos um autor e uma categoria primeiro!")
            return

        try:
            titulo = input("\nTítulo do livro: ").strip()

            print("\n--- Autores Disponíveis ---")
            for a in autores:
                cidade = self.cidades_db.buscar_cidade(a.cod_cidade)
                local = f"{cidade.descricao} - {cidade.estado}" if cidade else "Cidade desconhecida"
                print(f"{a.codigo} - {a.nome} ({local})")
            cod_autor = int(input("Código do autor: "))

            print("\n--- Categorias Disponíveis ---")
            for c in categorias:
                print(f"{c.codigo} - {c.descricao}")
            cod_categoria = int(input("Código da categoria: "))
            ano_publicacao = int(input("Ano de publicação: "))

            sucesso, msg = self.service.adicionar_livro(titulo, cod_autor, cod_categoria, ano_publicacao)
            print(msg)
        except ValueError:
            print("Código ou ano inválido.")

    def listar_livros(self):
        livros = self.service.listar_livros_completo()
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            for l in livros:
                print(l)
                print("-" * 50)

    def buscar_livro(self):
        try:
            codigo = int(input("Código do livro: "))
            livro = self.service.buscar_livro_completo(codigo)
            print(livro if livro else "Livro não encontrado.")
        except ValueError:
            print("Código inválido.")

    def remover_livro(self):
        try:
            codigo = int(input("Código do livro: "))
            sucesso, msg = self.service.remover_livro(codigo)
            print(msg)
        except ValueError:
            print("Código inválido.")
