from categorias.model import Categoria
from utils.busca import busca_binaria

class CategoriasDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.categorias = self.carregar_categorias()

    def carregar_categorias(self):
        categorias = []
        try:
            with open("txt/categorias.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    codigo, descricao = linha.strip().split("|")
                    categorias.append(Categoria(int(codigo), descricao))
            if categorias:
                self.ultimo_codigo = categorias[-1].codigo
        except FileNotFoundError:
            pass
        return categorias

    def salvar_categorias(self):
        with open("txt/categorias.txt", "w", encoding="utf-8") as f:
            for categoria in self.categorias:
                f.write(f"{categoria.codigo}|{categoria.descricao}\n")

    def adicionar_categoria(self, categoria: Categoria):
        if busca_binaria(self.categorias, categoria.codigo) != -1:
            return False
        self.categorias.append(categoria)
        self.ultimo_codigo = categoria.codigo
        self.salvar_categorias()
        return True

    def buscar_categoria(self, codigo):
        index = busca_binaria(self.categorias, codigo)
        return self.categorias[index] if index != -1 else None

    def remover_categoria(self, codigo):
        index = busca_binaria(self.categorias, codigo)
        if index == -1:
            return False
        del self.categorias[index]
        self.salvar_categorias()
        return True

    def listar_categorias(self):
        return self.categorias[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
