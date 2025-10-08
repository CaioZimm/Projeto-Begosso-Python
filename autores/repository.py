from autores.model import Autor

class AutoresDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.autores = self.carregar_autores()

    def carregar_autores(self):
        autores = []
        try:
            with open("txt/autores.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    codigo, nome, cod_cidade = linha.strip().split("|")
                    autores.append(Autor(int(codigo), nome, int(cod_cidade)))
            autores.sort(key=lambda a: a.codigo)
            if autores:
                self.ultimo_codigo = autores[-1].codigo
        except FileNotFoundError:
            pass
        return autores

    def salvar_autores(self):
        with open("txt/autores.txt", "w", encoding="utf-8") as f:
            for autor in self.autores:
                f.write(f"{autor.codigo}|{autor.nome}|{autor.cod_cidade}\n")

    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.autores) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.autores[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_autor(self, autor: Autor):
        if self._busca_binaria(autor.codigo) != -1:
            return False
        self.autores.append(autor)
        self.autores.sort(key=lambda a: a.codigo)
        self.ultimo_codigo = autor.codigo
        self.salvar_autores()
        return True

    def buscar_autor(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.autores[idx] if idx != -1 else None

    def remover_autor(self, codigo):
        idx = self._busca_binaria(codigo)
        if idx == -1:
            return False
        del self.autores[idx]
        self.salvar_autores()
        return True

    def listar_autores(self):
        return self.autores[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
