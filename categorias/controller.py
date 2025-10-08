from categorias.service import CategoriaService

class CategoriaController:
    def __init__(self, db):
        self.service = CategoriaService(db)

    def adicionar_categoria(self, descricao):
        return self.service.adicionar_categoria(descricao)

    def listar_categorias(self):
        return self.service.db.listar_categorias()

    def buscar_categoria(self, codigo):
        return self.service.db.buscar_categoria(codigo)

    def remover_categoria(self, codigo):
        return self.service.remover_categoria(codigo)
