# cidade.py
import csv

class NoCidade:
    def __init__(self, codigocidade, nomecidade, estado):
        self.codigocidade = codigocidade
        self.nomecidade = nomecidade
        self.estado = estado
        self.esquerda = None
        self.direita = None

class BuscaBinariaCidade:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigocidade, nomecidade, estado):
        if self.raiz is None:
            self.raiz = NoCidade(codigocidade, nomecidade, estado)
            return True
        return self._inserir(self.raiz, codigocidade, nomecidade, estado)

    def _inserir(self, no, codigocidade, nomecidade, estado):
        if codigocidade < no.codigocidade:
            if no.esquerda is None:
                no.esquerda = NoCidade(codigocidade, nomecidade, estado)
                return True
            return self._inserir(no.esquerda, codigocidade, nomecidade, estado)
        elif codigocidade > no.codigocidade:
            if no.direita is None:
                no.direita = NoCidade(codigocidade, nomecidade, estado)
                return True
            return self._inserir(no.direita, codigocidade, nomecidade, estado)
        else:
            return False

    def buscar(self, codigocidade):
        return self._buscar(self.raiz, codigocidade)

    def _buscar(self, no, codigocidade):
        if no is None:
            return None
        if codigocidade == no.codigocidade:
            return (no.codigocidade, no.nomecidade, no.estado)
        if codigocidade < no.codigocidade:
            return self._buscar(no.esquerda, codigocidade)
        return self._buscar(no.direita, codigocidade)

    def ordenar(self):
        resultado = []
        self._ordenar(self.raiz, resultado)
        return resultado

    def _ordenar(self, no, resultado):
        if no is not None:
            self._ordenar(no.esquerda, resultado)
            resultado.append((no.codigocidade, no.nomecidade, no.estado))
            self._ordenar(no.direita, resultado)

    def remover(self, codigocidade):
        self.raiz = self._remover(self.raiz, codigocidade)

    def _remover(self, no, codigocidade):
        if no is None:
            return None
        if codigocidade < no.codigocidade:
            no.esquerda = self._remover(no.esquerda, codigocidade)
        elif codigocidade > no.codigocidade:
            no.direita = self._remover(no.direita, codigocidade)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.codigocidade, no.nomecidade, no.estado = menor.codigocidade, menor.nomecidade, menor.estado
            no.direita = self._remover(no.direita, menor.codigocidade)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Cidade:
    def __init__(self, codigocidade, nomecidade, estado):
        self.codigocidade = str(codigocidade)
        self.nomecidade = nomecidade
        self.estado = estado

    def __str__(self):
        return f"{self.codigocidade} - {self.nomecidade} ({self.estado})"

class CidadesDB:
    def __init__(self):
        self.arvore = BuscaBinariaCidade()
        self.codigos_existentes = set()

    def adicionarcidade(self, cidade: Cidade):
        if cidade.codigocidade in self.codigos_existentes:
            return False
        if self.arvore.inserir(int(cidade.codigocidade), cidade.nomecidade, cidade.estado):
            self.codigos_existentes.add(cidade.codigocidade)
            return True
        return False

    def listarcidades(self):
        return self.arvore.ordenar()

    def buscarcidade(self, codigocidade):
        if codigocidade is None:
            return None
        return self.arvore.buscar(int(str(codigocidade)))

    def removercidade(self, codigocidade):
        if self.buscarcidade(codigocidade):
            self.arvore.remover(int(str(codigocidade)))
            self.codigos_existentes.discard(str(codigocidade))
            return True
        return False

    def salvar_para_txt(self, caminho="cidades.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["codigocidade", "nomecidade", "estado"])
            for cod, nome, uf in self.listarcidades():
                w.writerow([cod, nome, uf])

    def carregar_de_txt(self, caminho="cidades.txt", limpar_antes=False):
        if limpar_antes:
            self.arvore = BuscaBinariaCidade()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f, delimiter=";")
                linhas = list(r)
                if linhas and linhas[0] and str(linhas[0][0]).strip().lower() == "codigocidade":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 3:
                        continue
                    try:
                        int(str(row[0]))
                    except ValueError:
                        continue
                    c = Cidade(row[0], row[1], row[2])
                    self.adicionarcidade(c)
        except FileNotFoundError:
            pass
