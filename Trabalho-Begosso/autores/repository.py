import bisect
from autores.model import Autor

class AutoresDB:
    def __init__(self):
        self.autores = []
        self.ultimo_codigo = 0

    def adicionar_autor(self, autor: Autor):
        index = bisect.bisect_left(self.autores, autor)
        if index < len(self.autores) and self.autores[index].codigo == autor.codigo:
            return False
        self.autores.insert(index, autor)
        self.ultimo_codigo = autor.codigo
        return True

    def buscar_autor(self, codigo):
        fake = Autor(codigo, "", "")
        index = bisect.bisect_left(self.autores, fake)
        if index < len(self.autores) and self.autores[index].codigo == codigo:
            return self.autores[index]
        return None

    def remover_autor(self, codigo):
        autor = self.buscar_autor(codigo)
        if autor:
            self.autores.remove(autor)
            return True
        return False

    def listar_autores(self):
        return self.autores[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
