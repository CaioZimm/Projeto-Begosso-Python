from categorias.model import Categoria

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
            categorias.sort(key=lambda c: c.codigo)
            if categorias:
                self.ultimo_codigo = categorias[-1].codigo
        except FileNotFoundError:
            pass
        return categorias

    def salvar_categorias(self):
        with open("txt/categorias.txt", "w", encoding="utf-8") as f:
            for categoria in self.categorias:
                f.write(f"{categoria.codigo}|{categoria.descricao}\n")

    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.categorias) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.categorias[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_categoria(self, categoria: Categoria):
        if self._busca_binaria(categoria.codigo) != -1:
            return False
        self.categorias.append(categoria)
        self.categorias.sort(key=lambda c: c.codigo)
        self.ultimo_codigo = categoria.codigo
        self.salvar_categorias()
        return True

    def buscar_categoria(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.categorias[idx] if idx != -1 else None

    def remover_categoria(self, codigo):
        idx = self._busca_binaria(codigo)
        if idx == -1:
            return False
        del self.categorias[idx]
        self.salvar_categorias()
        return True

    def listar_categorias(self):
        return self.categorias[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
