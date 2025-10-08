# categorias.py
import csv

class NoCategoria:
    def __init__(self, codigocategoria, nomecategoria):
        self.codigocategoria = int(codigocategoria)
        self.nomecategoria = nomecategoria
        self.esquerda = None
        self.direita = None

class ArvoreCategorias:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigocategoria, nomecategoria):
        if self.raiz is None:
            self.raiz = NoCategoria(codigocategoria, nomecategoria)
            return True
        return self._inserir(self.raiz, codigocategoria, nomecategoria)

    def _inserir(self, no, codigocategoria, nomecategoria):
        if codigocategoria < no.codigocategoria:
            if no.esquerda is None:
                no.esquerda = NoCategoria(codigocategoria, nomecategoria)
                return True
            return self._inserir(no.esquerda, codigocategoria, nomecategoria)
        elif codigocategoria > no.codigocategoria:
            if no.direita is None:
                no.direita = NoCategoria(codigocategoria, nomecategoria)
                return True
            return self._inserir(no.direita, codigocategoria, nomecategoria)
        else:
            return False

    def buscar(self, codigocategoria):
        return self._buscar(self.raiz, codigocategoria)

    def _buscar(self, no, codigocategoria):
        if no is None:
            return None
        if codigocategoria == no.codigocategoria:
            return no.nomecategoria
        if codigocategoria < no.codigocategoria:
            return self._buscar(no.esquerda, codigocategoria)
        return self._buscar(no.direita, codigocategoria)

    def listar(self):
        res = []
        self._ordenar(self.raiz, res)
        return res

    def _ordenar(self, no, res):
        if no:
            self._ordenar(no.esquerda, res)
            res.append((no.codigocategoria, no.nomecategoria))
            self._ordenar(no.direita, res)

    def remover(self, codigocategoria):
        self.raiz = self._remover(self.raiz, codigocategoria)

    def _remover(self, no, codigocategoria):
        if no is None:
            return None
        if codigocategoria < no.codigocategoria:
            no.esquerda = self._remover(no.esquerda, codigocategoria)
        elif codigocategoria > no.codigocategoria:
            no.direita = self._remover(no.direita, codigocategoria)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.codigocategoria, no.nomecategoria = menor.codigocategoria, menor.nomecategoria
            no.direita = self._remover(no.direita, menor.codigocategoria)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Categoria:
    def __init__(self, codigocategoria, nomecategoria):
        self.codigocategoria = str(codigocategoria)
        self.nomecategoria = nomecategoria

    def __str__(self):
        return f"{self.codigocategoria} - {self.nomecategoria}"

class CategoriasDB:
    def __init__(self):
        self.arvore = ArvoreCategorias()
        self.codigos_existentes = set()

    def adicionarcategoria(self, categoria):
        chave = str(categoria.codigocategoria)
        if chave in self.codigos_existentes:
            return False
        if self.arvore.inserir(int(chave), categoria.nomecategoria):
            self.codigos_existentes.add(chave)
            return True
        return False

    def listarcategorias(self):
        return self.arvore.listar()

    def buscarcategoria(self, codigocategoria):
        if codigocategoria is None:
            return None
        return self.arvore.buscar(int(str(codigocategoria)))

    def removercategoria(self, codigocategoria):
        if self.buscarcategoria(codigocategoria):
            self.arvore.remover(int(str(codigocategoria)))
            self.codigos_existentes.discard(str(codigocategoria))
            return True
        return False

    def salvar_para_txt(self, caminho="categorias.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["codigocategoria", "nomecategoria"])
            for cod, nome in self.listarcategorias():
                w.writerow([cod, nome])

    def carregar_de_txt(self, caminho="categorias.txt", limpar_antes=False):
        if limpar_antes:
            self.arvore = ArvoreCategorias()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f, delimiter=";")
                linhas = list(r)
                if linhas and linhas[0] and str(linhas[0][0]).strip().lower() == "codigocategoria":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 2:
                        continue
                    try:
                        int(str(row[0]))
                    except ValueError:
                        continue
                    c = Categoria(row[0], row[1])
                    self.adicionarcategoria(c)
        except FileNotFoundError:
            pass
