from categorias.service import CategoriaService

class CategoriaController:
    def __init__(self, categorias_db):
        self.service = CategoriaService(categorias_db)

    def adicionar_categoria(self):
        descricao = input("Descrição da categoria: ").strip()
        sucesso, msg = self.service.adicionar_categoria(descricao)
        print(msg)

    def listar_categorias(self):
        categorias = self.service.db.listar_categorias()
        if not categorias:
            print("Nenhuma categoria cadastrada.")
        else:
            for c in categorias:
                print(c)

    def buscar_categoria(self):
        try:
            codigo = int(input("Código da categoria: "))
            categoria = self.service.db.buscar_categoria(codigo)
            print(categoria if categoria else "Categoria não encontrada.")
        except ValueError:
            print("Código inválido.")

    def remover_categoria(self):
        try:
            codigo = int(input("Código da categoria: "))
            sucesso, msg = self.service.remover_categoria(codigo)
            print(msg)
        except ValueError:
            print("Código inválido.")
