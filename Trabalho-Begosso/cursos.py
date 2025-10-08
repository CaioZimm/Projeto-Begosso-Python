# curso.py
import csv

class NoCurso:
    def __init__(self, curso):
        self.curso = curso
        self.esquerda = None
        self.direita = None

class BuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, curso: 'Curso'):
        if self.raiz is None:
            self.raiz = NoCurso(curso)
            return True
        return self._inserir(self.raiz, curso)

    def _inserir(self, no, curso: 'Curso'):
        if curso.codigocurso < no.curso.codigocurso:
            if no.esquerda is None:
                no.esquerda = NoCurso(curso)
                return True
            return self._inserir(no.esquerda, curso)
        elif curso.codigocurso > no.curso.codigocurso:
            if no.direita is None:
                no.direita = NoCurso(curso)
                return True
            return self._inserir(no.direita, curso)
        else:
            return False

    def buscar(self, codigocurso):
        return self._buscar(self.raiz, codigocurso)

    def _buscar(self, no, codigocurso):
        if no is None:
            return None
        if codigocurso == no.curso.codigocurso:
            return no.curso
        elif codigocurso < no.curso.codigocurso:
            return self._buscar(no.esquerda, codigocurso)
        else:
            return self._buscar(no.direita, codigocurso)

    def ordernar(self):
        res = []
        self._ordenar(self.raiz, res)
        return res

    def _ordenar(self, no, res):
        if no is not None:
            self._ordenar(no.esquerda, res)
            res.append(no.curso)
            self._ordenar(no.direita, res)

    def remover(self, codigocurso):
        self.raiz = self._remover(self.raiz, codigocurso)

    def _remover(self, no, codigocurso):
        if no is None:
            return None
        if codigocurso < no.curso.codigocurso:
            no.esquerda = self._remover(no.esquerda, codigocurso)
        elif codigocurso > no.curso.codigocurso:
            no.direita = self._remover(no.direita, codigocurso)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.curso = menor.curso
            no.direita = self._remover(no.direita, menor.curso.codigocurso)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Curso:
    def __init__(self, codigocurso, nomecurso):
        self.codigocurso = int(codigocurso)
        self.nomecurso = nomecurso

    def __str__(self):
        return f"{self.codigocurso} - Curso: {self.nomecurso}"

class CursosDB:
    def __init__(self):
        self.cursos = BuscaBinaria()
        self.codigos_existentes = set()

    def adicionarcurso(self, curso: Curso):
        if curso.codigocurso in self.codigos_existentes:
            return False
        if self.cursos.inserir(curso):
            self.codigos_existentes.add(curso.codigocurso)
            return True
        return False

    def listarcursos(self):
        return self.cursos.ordernar()

    def buscarcurso(self, codigocurso):
        return self.cursos.buscar(int(codigocurso))

    def removercurso(self, codigocurso):
        cod = int(codigocurso)
        if cod in self.codigos_existentes:
            self.cursos.remover(cod)
            self.codigos_existentes.remove(cod)
            return True
        return False

    def salvar_para_txt(self, caminho="cursos.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["codigocurso", "nomecurso"])
            for curso in self.listarcursos():
                w.writerow([curso.codigocurso, curso.nomecurso])

    def carregar_de_txt(self, caminho="cursos.txt", limpar_antes=False):
        if limpar_antes:
            self.cursos = BuscaBinaria()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f, delimiter=";")
                linhas = list(r)
                if linhas and linhas[0] and str(linhas[0][0]).strip().lower() == "codigocurso":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 2:
                        continue
                    try:
                        int(row[0])
                    except ValueError:
                        continue
                    c = Curso(row[0], row[1])
                    self.adicionarcurso(c)
        except FileNotFoundError:
            pass
