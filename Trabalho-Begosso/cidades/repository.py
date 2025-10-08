import bisect
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
                    cidade = Cidade(int(codigo), descricao, estado)
                    cidades.append(cidade)
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
        index = bisect.bisect_left(self.cidades, cidade)
        if index < len(self.cidades) and self.cidades[index].codigo == cidade.codigo:
            return False
        self.cidades.insert(index, cidade)
        self.ultimo_codigo = cidade.codigo
        self.salvar_cidades()
        return True

    def buscar_cidade(self, codigo):
        fake = Cidade(codigo, "", "")
        index = bisect.bisect_left(self.cidades, fake)
        if index < len(self.cidades) and self.cidades[index].codigo == codigo:
            return self.cidades[index]
        return None

    def remover_cidade(self, codigo):
        cidade = self.buscar_cidade(codigo)
        if cidade:
            self.cidades.remove(cidade)
            self.salvar_cidades()
            return True
        return False

    def listar_cidades(self):
        return self.cidades[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo