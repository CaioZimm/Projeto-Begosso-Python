from cidades.model import Cidade

class CidadesDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.cidades = self.carregar_cidades()

    def carregar_cidades(self):
        cidades = []
        try:
            with open("txt/cidades.txt", "r") as f:
                for linha in f:
                    codigo, descricao, estado = linha.strip().split("|")
                    cidades.append(Cidade(int(codigo), descricao, estado))
            cidades.sort(key=lambda c: c.codigo)
            if cidades:
                self.ultimo_codigo = cidades[-1].codigo
        except FileNotFoundError:
            pass
        return cidades

    def salvar_cidades(self):
        with open("txt/cidades.txt", "w") as f:
            for cidade in self.cidades:
                f.write(f"{cidade.codigo}|{cidade.descricao}|{cidade.estado}\n")

    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.cidades) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.cidades[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_cidade(self, cidade: Cidade):
        if self._busca_binaria(cidade.codigo) != -1:
            return False

        self.cidades.append(cidade)
        self.cidades.sort(key=lambda c: c.codigo)
        self.ultimo_codigo = cidade.codigo
        self.salvar_cidades()
        return True

    def buscar_cidade(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.cidades[idx] if idx != -1 else None

    def remover_cidade(self, codigo):
        idx = self._busca_binaria(codigo)
        if idx == -1:
            return False
        del self.cidades[idx]
        self.salvar_cidades()
        return True

    def listar_cidades(self):
        return self.cidades[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo