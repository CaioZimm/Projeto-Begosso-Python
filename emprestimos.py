# emprestimos.py
import csv
from datetime import date, timedelta

class NoEmprestimo:
    def __init__(self, codigo, emprestimo):
        self.codigo = codigo
        self.emprestimo = emprestimo
        self.esquerda = None
        self.direita = None

class ArvoreEmprestimos:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, emprestimo):
        if self.raiz is None:
            self.raiz = NoEmprestimo(codigo, emprestimo)
            return True
        return self._inserir(self.raiz, codigo, emprestimo)

    def _inserir(self, no, codigo, emprestimo):
        if codigo < no.codigo:
            if no.esquerda is None:
                no.esquerda = NoEmprestimo(codigo, emprestimo)
                return True
            return self._inserir(no.esquerda, codigo, emprestimo)
        elif codigo > no.codigo:
            if no.direita is None:
                no.direita = NoEmprestimo(codigo, emprestimo)
                return True
            return self._inserir(no.direita, codigo, emprestimo)
        else:
            return False

    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, no, codigo):
        if no is None:
            return None
        if codigo == no.codigo:
            return no.emprestimo
        if codigo < no.codigo:
            return self._buscar(no.esquerda, codigo)
        return self._buscar(no.direita, codigo)

    def listar(self):
        res = []
        self._ordenar(self.raiz, res)
        return res

    def _ordenar(self, no, res):
        if no:
            self._ordenar(no.esquerda, res)
            res.append(no.emprestimo)
            self._ordenar(no.direita, res)

    def remover(self, codigo):
        self.raiz = self._remover(self.raiz, codigo)

    def _remover(self, no, codigo):
        if no is None:
            return None
        if codigo < no.codigo:
            no.esquerda = self._remover(no.esquerda, codigo)
        elif codigo > no.codigo:
            no.direita = self._remover(no.direita, codigo)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.codigo, no.emprestimo = menor.codigo, menor.emprestimo
            no.direita = self._remover(no.direita, menor.codigo)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Emprestimo:
    def __init__(self, codigoemprestimo, codigolivro, codigoaluno, data_emprestimo=None, data_devolucao=None, devolvido=False):
        self.codigoemprestimo = str(codigoemprestimo)
        self.codigolivro = str(codigolivro)
        self.codigoaluno = str(codigoaluno)
        self.data_emprestimo = data_emprestimo or date.today()
        self.data_devolucao = data_devolucao or (self.data_emprestimo + timedelta(days=7))
        self.devolvido = bool(devolvido)

    def __str__(self):
        dev = "Sim" if self.devolvido else "Não"
        return (f"{self.codigoemprestimo} - Livro {self.codigolivro} - Aluno {self.codigoaluno} | "
                f"Emp: {self.data_emprestimo.isoformat()} Dev: {self.data_devolucao.isoformat()} Devolvido: {dev}")

class EmprestimosDB:
    def __init__(self):
        self.arvore = ArvoreEmprestimos()
        self.codigos_existentes = set()

    def adicionaremprestimo(self, emprestimo):
        chave = str(emprestimo.codigoemprestimo)
        if chave in self.codigos_existentes:
            return False
        if self.arvore.inserir(int(chave), emprestimo):
            self.codigos_existentes.add(chave)
            return True
        return False

    def listaremprestimos(self):
        return self.arvore.listar()

    def buscaremprestimo(self, codigoemprestimo):
        if codigoemprestimo is None:
            return None
        return self.arvore.buscar(int(str(codigoemprestimo)))

    def removeremprestimo(self, codigoemprestimo):
        if self.buscaremprestimo(codigoemprestimo):
            self.arvore.remover(int(str(codigoemprestimo)))
            self.codigos_existentes.discard(str(codigoemprestimo))
            return True
        return False

    def emprestimos_ativos(self):
        return [e for e in self.listaremprestimos() if not e.devolvido]

    def emprestimos_atrasados(self, hoje=None):
        hoje = hoje or date.today()
        return [e for e in self.emprestimos_ativos() if e.data_devolucao < hoje]

    def contar_por_periodo(self, data_inicio, data_fim):
        return len([e for e in self.listaremprestimos() if data_inicio <= e.data_emprestimo <= data_fim])

    def salvar_para_txt(self, caminho="emprestimos.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["codigoemprestimo", "codigolivro", "codigoaluno", "data_emprestimo", "data_devolucao", "devolvido"])
            for e in self.listaremprestimos():
                w.writerow([e.codigoemprestimo, e.codigolivro, e.codigoaluno, e.data_emprestimo.isoformat(), e.data_devolucao.isoformat(), int(e.devolvido)])

    def carregar_de_txt(self, caminho="emprestimos.txt", limpar_antes=False):
        if limpar_antes:
            self.arvore = ArvoreEmprestimos()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f, delimiter=";")
                linhas = list(r)
                if linhas and linhas[0] and str(linhas[0][0]).strip().lower() == "codigoemprestimo":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 6:
                        continue
                    e = Emprestimo(
                        row[0],
                        row[1],
                        row[2],
                        date.fromisoformat(row[3]),
                        date.fromisoformat(row[4]),
                        bool(int(row[5]))
                    )
                    self.adicionaremprestimo(e)
        except FileNotFoundError:
            pass
