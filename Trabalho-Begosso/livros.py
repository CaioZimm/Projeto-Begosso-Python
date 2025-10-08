# livros.py
import csv

class NoLivro:
    def __init__(self, livro):
        self.livro = livro
        self.codigolivro = int(livro.codigolivro)
        self.esquerda = None
        self.direita = None

class ArvoreLivros:
    def __init__(self):
        self.raiz = None

    def inserir(self, livro):
        if self.raiz is None:
            self.raiz = NoLivro(livro)
            return True
        return self._inserir(self.raiz, livro)

    def _inserir(self, no, livro):
        chave = int(livro.codigolivro)
        if chave < no.codigolivro:
            if no.esquerda is None:
                no.esquerda = NoLivro(livro)
                return True
            return self._inserir(no.esquerda, livro)
        elif chave > no.codigolivro:
            if no.direita is None:
                no.direita = NoLivro(livro)
                return True
            return self._inserir(no.direita, livro)
        else:
            return False

    def buscar(self, codigolivro):
        if codigolivro is None:
            return None
        return self._buscar(self.raiz, int(str(codigolivro)))

    def _buscar(self, no, chave):
        if no is None:
            return None
        if chave == no.codigolivro:
            return no.livro
        if chave < no.codigolivro:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)

    def listar(self):
        res = []
        self._ordenar(self.raiz, res)
        return res

    def _ordenar(self, no, res):
        if no:
            self._ordenar(no.esquerda, res)
            res.append(no.livro)
            self._ordenar(no.direita, res)

    def remover(self, codigolivro):
        self.raiz = self._remover(self.raiz, int(str(codigolivro)))

    def _remover(self, no, chave):
        if no is None:
            return None
        if chave < no.codigolivro:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.codigolivro:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            menor = self._minimo(no.direita)
            no.livro = menor.livro
            no.codigolivro = menor.codigolivro
            no.direita = self._remover(no.direita, menor.codigolivro)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

class Livro:
    def __init__(self, codigolivro, titulo, codigoautor, codigocategoria, ano_publicacao, disponibilidade=True):
        self.codigolivro = str(codigolivro)
        self.titulo = titulo
        self.codigoautor = str(codigoautor)
        self.codigocategoria = str(codigocategoria)
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = bool(disponibilidade)

    def __str__(self):
        dispo = "Disponível" if self.disponibilidade else "Emprestado"
        return f"{self.codigolivro} - {self.titulo} (Autor {self.codigoautor} | Cat {self.codigocategoria}) - {dispo}"

class LivrosDB:
    def __init__(self):
        self.arvore = ArvoreLivros()
        self.codigos_existentes = set()

    def adicionarlivro(self, livro):
        chave = str(livro.codigolivro)
        if chave in self.codigos_existentes:
            return False
        if self.arvore.inserir(livro):
            self.codigos_existentes.add(chave)
            return True
        return False

    def listarlivros(self):
        return self.arvore.listar()

    def buscarlivro(self, codigolivro):
        return self.arvore.buscar(codigolivro)

    def removerlivro(self, codigolivro):
        if self.buscarlivro(codigolivro):
            self.arvore.remover(codigolivro)
            self.codigos_existentes.discard(str(codigolivro))
            return True
        return False

    def marcar_emprestado(self, codigolivro):
        livro = self.buscarlivro(codigolivro)
        if livro and livro.disponibilidade:
            livro.disponibilidade = False
            return True
        return False

    def marcar_disponivel(self, codigolivro):
        livro = self.buscarlivro(codigolivro)
        if livro and not livro.disponibilidade:
            livro.disponibilidade = True
            return True
        return False

    def salvar_para_txt(self, caminho="livros.txt"):
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["codigolivro", "titulo", "codigoautor", "codigocategoria", "ano_publicacao", "disponibilidade"])
            for l in self.listarlivros():
                w.writerow([l.codigolivro, l.titulo, l.codigoautor, l.codigocategoria, l.ano_publicacao, int(l.disponibilidade)])

    def carregar_de_txt(self, caminho="livros.txt", limpar_antes=False):
        if limpar_antes:
            self.arvore = ArvoreLivros()
            self.codigos_existentes.clear()
        try:
            with open(caminho, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f, delimiter=";")
                linhas = list(r)
                if linhas and linhas[0] and str(linhas[0][0]).strip().lower() == "codigolivro":
                    linhas = linhas[1:]
                for row in linhas:
                    if len(row) < 6:
                        continue
                    try:
                        int(row[0])
                    except ValueError:
                        continue
                    disponibilidade = bool(int(row[5]))
                    livro = Livro(row[0], row[1], row[2], row[3], row[4], disponibilidade)
                    self.adicionarlivro(livro)
        except FileNotFoundError:
            pass
