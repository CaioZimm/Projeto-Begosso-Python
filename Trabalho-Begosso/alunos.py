# alunos.py
import csv

class NoAluno:
    def __init__(self, aluno):
        self.aluno = aluno
        self.esquerda = None
        self.direita = None

class BuscaBinariaAluno:
    def __init__(self):
        self.raiz = None

    def inserir(self, aluno):
        if self.raiz is None:
            self.raiz = NoAluno(aluno)
            return True
        return self._inserir(self.raiz, aluno)
    
    def _inserir(self, no, aluno):
        if aluno.codigoaluno < no.aluno.codigoaluno:
            if no.esquerda is None:
                no.esquerda = NoAluno(aluno)
                return True
            return self._inserir(no.esquerda, aluno)
        elif aluno.codigoaluno > no.aluno.codigoaluno:
            if no.direita is None:
                no.direita = NoAluno(aluno)
                return True
            return self._inserir(no.direita, aluno)
        else:
            return False

    def buscar(self, codigoaluno):
        return self._buscar(self.raiz, codigoaluno)

    def _buscar(self, no, codigoaluno):
        if no is None:
            return None
        if codigoaluno == no.aluno.codigoaluno:
            return no.aluno
        if codigoaluno < no.aluno.codigoaluno:
            return self._buscar(no.esquerda, codigoaluno)
        return self._buscar(no.direita, codigoaluno)

    def listar(self):
        res = []
        self._ordenar(self.raiz, res)
        return res

    def _ordenar(self, no, res):
        if no:
            self._ordenar(no.esquerda, res)
            res.append(no.aluno)
            self._ordenar(no.direita, res)

    def remover(self, codigoaluno):
        self.raiz = self._remover(self.raiz, codigoaluno)

    def _remover(self, no, codigoaluno):
        if no is None:
            return None
        if codigoaluno < no.aluno.codigoaluno:
            no.esquerda = self._remover(no.esquerda, codigoaluno)
        elif codigoaluno > no.aluno.codigoaluno:
            no.direita = self._remover(no.direita, codigoaluno)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.aluno = menor.aluno
            no.direita = self._remover(no.direita, menor.aluno.codigoaluno)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Aluno:
    def __init__(self, codigoaluno, nomealuno, codigocurso, codigocidade):
        self.codigoaluno = int(codigoaluno)
        self.nomealuno = nomealuno
        self.codigocurso = int(codigocurso)
        self.codigocidade = int(codigocidade)

    def __str__(self):
        return f"{self.codigoaluno} - {self.nomealuno} (Curso {self.codigocurso}, Cidade {self.codigocidade})"

class AlunosDB:
    def __init__(self):
        self.arvore = BuscaBinariaAluno()
        self.codigos_existentes = set()

    def adicionaraluno(self, aluno):
        chave = int(aluno.codigoaluno)
        if chave in self.codigos_existentes:
            return False
        if self.arvore.inserir(aluno):
            self.codigos_existentes.add(chave)
            return True
        return False

    def listaralunos(self):
        return self.arvore.listar()

    def buscaraluno(self, codigoaluno):
        if codigoaluno is None:
            return None
        return self.arvore.buscar(int(codigoaluno))

    def removeraluno(self, codigoaluno):
        if self.buscaraluno(codigoaluno):
            self.arvore.remover(int(codigoaluno))
            self.codigos_existentes.discard(int(codigoaluno))
            return True
        return False

    def salvar_para_txt(self, caminho="alunos.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["codigoaluno", "nomealuno", "codigocurso", "codigocidade"])
            for aluno in self.listaralunos():
                writer.writerow([aluno.codigoaluno, aluno.nomealuno, aluno.codigocurso, aluno.codigocidade])

    def carregar_de_txt(self, caminho="alunos.txt", limpar_antes=False):
        if limpar_antes:
            self.arvore = BuscaBinariaAluno()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f, delimiter=";")
                linhas = list(reader)
                if linhas and linhas[0] and linhas[0][0].strip().lower() == "codigoaluno":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 4:
                        continue
                    try:
                        aluno = Aluno(row[0], row[1], row[2], row[3])
                    except ValueError:
                        continue
                    self.adicionaraluno(aluno)
        except FileNotFoundError:
            pass
