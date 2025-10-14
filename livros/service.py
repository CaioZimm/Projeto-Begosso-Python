from livros.model import Livro
from livros.repository import LivrosDB
from autores.repository import AutoresDB
from categorias.repository import CategoriasDB
from cidades.repository import CidadesDB

class LivroService:
    def __init__(self, db: LivrosDB):
        self.db = db
        self.autores_db = AutoresDB()
        self.categorias_db = CategoriasDB()
        self.cidades_db = CidadesDB()

    def validar_dados(self, titulo, cod_autor, cod_categoria, ano_publicacao):
        if not titulo.strip():
            return False, "O título é obrigatório."
        if not str(ano_publicacao).isdigit():
            return False, "O ano de publicação deve ser um número."
        if not self.autores_db.listar_autores():
            return False, "Precisa cadastrar pelo menos um autor primeiro."
        if not self.categorias_db.listar_categorias():
            return False, "Precisa cadastrar pelo menos uma categoria primeiro."
        autor = self.autores_db.buscar_autor(cod_autor)
        categoria = self.categorias_db.buscar_categoria(cod_categoria)
        if not autor:
            return False, "Código de autor inválido."
        if not categoria:
            return False, "Código de categoria inválido."
        return True, "Validação correta"

    def adicionar_livro(self, titulo, cod_autor, cod_categoria, ano_publicacao):
        valido, msg = self.validar_dados(titulo, cod_autor, cod_categoria, ano_publicacao)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        livro = Livro(codigo, titulo.strip(), cod_autor, cod_categoria, int(ano_publicacao))
        sucesso = self.db.adicionar_livro(livro)
        if sucesso:
            return True, f"Livro {titulo} - código {codigo} adicionado com sucesso!"
        return False, "Error"

    def remover_livro(self, codigo):
        livro = self.db.buscar_livro(codigo)
        if not livro:
            return False, "Livro não encontrado."
        sucesso = self.db.remover_livro(codigo)
        if sucesso:
            return True, f"Livro {livro.titulo} - {livro.codigo} removido com sucesso!"
        return False, "Error"

    def listar_livros_completo(self):
        livros = self.db.listar_livros()
        resultado = []
        for l in livros:
            autor = self.autores_db.buscar_autor(l.cod_autor)
            categoria = self.categorias_db.buscar_categoria(l.cod_categoria)
            cidade = self.cidades_db.buscar_cidade(autor.cod_cidade) if autor else None

            nome_autor = autor.nome if autor else "Autor não encontrado"
            cidade_autor = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade desconhecida"
            nome_categoria = categoria.descricao if categoria else "Categoria não encontrada"

            resultado.append(
                f"{l.codigo} - {l.titulo} ({l.ano_publicacao})\n"
                f"   Autor: {nome_autor} - {cidade_autor}\n"
                f"   Categoria: {nome_categoria}\n"
                f"   Disponibilidade: {l.disponibilidade}"
            )
        return resultado

    def buscar_livro_completo(self, codigo):
        l = self.db.buscar_livro(codigo)
        if not l:
            return None

        autor = self.autores_db.buscar_autor(l.cod_autor)
        categoria = self.categorias_db.buscar_categoria(l.cod_categoria)
        cidade = self.cidades_db.buscar_cidade(autor.cod_cidade) if autor else None

        nome_autor = autor.nome if autor else "Autor não encontrado"
        cidade_autor = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade desconhecida"
        nome_categoria = categoria.descricao if categoria else "Categoria não encontrada"

        return (
            f"{l.codigo} - {l.titulo} ({l.ano_publicacao})\n"
            f"   Autor: {nome_autor} - {cidade_autor}\n"
            f"   Categoria: {nome_categoria}\n"
            f"   Disponibilidade: {l.disponibilidade}"
        )
