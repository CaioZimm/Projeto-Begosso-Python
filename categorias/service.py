from categorias.model import Categoria
from categorias.repository import CategoriasDB

class CategoriaService:
    def __init__(self, db: CategoriasDB):
        self.db = db
        self.categorias_db = CategoriasDB()

    def validar_categoria(self, descricao):
        if not descricao.strip():
            return False, "A descrição da categoria é obrigatória."
        return True, "Validação correta"

    def adicionar_categoria(self, descricao):
        valido, msg = self.validar_categoria(descricao)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        categoria = Categoria(codigo, descricao.strip())
        sucesso = self.db.adicionar_categoria(categoria)
        if sucesso:
            return True, f"Categoria {descricao} -  código {codigo} cadastrada com sucesso!"
        return False, "Error"

    def remover_categoria(self, codigo):
        categoria = self.db.buscar_categoria(codigo)
        if not categoria:
            return False, "Categoria não encontrada."

        sucesso = self.db.remover_categoria(codigo)
        if sucesso:
            return True, f"Categoria {categoria.descricao} - {categoria.codigo} removida com sucesso!"
        return False, "Error"
