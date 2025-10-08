# autores.py
import csv

class NoAutor:
    def __init__(self, autor):
        self.autor = autor
        self.esquerda = None
        self.direita = None

class ArvoreAutores:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, autor):
        if self.raiz is None:
            self.raiz = NoAutor(autor)
            return True
        return self._inserir(self.raiz, chave, autor)

    def _inserir(self, no, chave, autor):
        if chave < int(no.autor.codigoautor):
            if no.esquerda is None:
                no.esquerda = NoAutor(autor)
                return True
            return self._inserir(no.esquerda, chave, autor)
        elif chave > int(no.autor.codigoautor):
            if no.direita is None:
                no.direita = NoAutor(autor)
                return True
            return self._inserir(no.direita, chave, autor)
        else:
            return False

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if no is None:
            return None
        if chave == int(no.autor.codigoautor):
            return no.autor
        if chave < int(no.autor.codigoautor):
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)

    def listar(self):
        res = []
        self._ordenar(self.raiz, res)
        return res

    def _ordenar(self, no, res):
        if no:
            self._ordenar(no.esquerda, res)
            res.append(no.autor)
            self._ordenar(no.direita, res)

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return None
        if chave < int(no.autor.codigoautor):
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > int(no.autor.codigoautor):
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.autor = menor.autor
            no.direita = self._remover(no.direita, int(menor.autor.codigoautor))
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Autor:
    def __init__(self, codigoautor, nomeautor, codigocidade):
        self.codigoautor = str(codigoautor)
        self.nomeautor = nomeautor
        self.codigocidade = str(codigocidade)

    def __str__(self):
        return f"{self.codigoautor} - {self.nomeautor} (Cidade {self.codigocidade})"

class AutoresDB:
    def __init__(self):
        self.arvore = ArvoreAutores()
        self.codigos_existentes = set()

    def adicionarautor(self, autor):
        chave = str(autor.codigoautor)
        if chave in self.codigos_existentes:
            return False
        if self.arvore.inserir(int(chave), autor):
            self.codigos_existentes.add(chave)
            return True
        return False

    def listarautores(self):
        return self.arvore.listar()

    def buscarautor(self, codigoautor):
        if codigoautor is None:
            return None
        return self.arvore.buscar(int(str(codigoautor)))

    def removerautor(self, codigoautor):
        if self.buscarautor(codigoautor):
            self.arvore.remover(int(str(codigoautor)))
            self.codigos_existentes.discard(str(codigoautor))
            return True
        return False

    def salvar_para_txt(self, caminho="autores.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["codigoautor", "nomeautor", "codigocidade"])
            for a in self.listarautores():
                w.writerow([a.codigoautor, a.nomeautor, a.codigocidade])

    def carregar_de_txt(self, caminho="autores.txt", limpar_antes=False):
        if limpar_antes:
            self.arvore = ArvoreAutores()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f, delimiter=";")
                linhas = list(r)
                if linhas and linhas[0] and str(linhas[0][0]).strip().lower() == "codigoautor":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 3:
                        continue
                    try:
                        int(str(row[0]))
                    except ValueError:
                        continue
                    a = Autor(row[0], row[1], row[2])
                    self.adicionarautor(a)
        except FileNotFoundError:
            pass
