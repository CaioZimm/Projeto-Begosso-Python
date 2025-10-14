from cidades.model import Cidade
from utils.busca import busca_binaria

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
            if cidades:
                self.ultimo_codigo = cidades[-1].codigo
        except FileNotFoundError:
            pass
        return cidades

    def salvar_cidades(self):
        with open("txt/cidades.txt", "w") as f:
            for cidade in self.cidades:
                f.write(f"{cidade.codigo}|{cidade.descricao}|{cidade.estado}\n")

    def adicionar_cidade(self, cidade: Cidade):
        if busca_binaria(self.cidades, cidade.codigo) != -1:
            return False

        self.cidades.append(cidade)
        self.ultimo_codigo = cidade.codigo
        self.salvar_cidades()

        self.cidades = self.carregar_cidades()
        return True

    def buscar_cidade(self, codigo):
        index = busca_binaria(self.cidades, codigo)
        return self.cidades[index] if index != -1 else None

    def remover_cidade(self, codigo):
        index = busca_binaria(self.cidades, codigo)
        if index == -1:
            return False
        del self.cidades[index]
        self.salvar_cidades()
        return True

    def listar_cidades(self):
        return self.cidades[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo