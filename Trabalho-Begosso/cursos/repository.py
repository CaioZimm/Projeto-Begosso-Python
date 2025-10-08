from cursos.model import Curso
import bisect

class CursosDB:
    def __init__(self):
        self.cursos = []

    def __ordenar(self):
        self.cursos.sort(key=lambda c: c.codigocurso)

    def __posicao_insercao(self, codigocurso):
        # Retorna o índice onde o curso deveria estar
        return bisect.bisect_left([c.codigocurso for c in self.cursos], codigocurso)

    def adicionarcurso(self, curso):
        if self.buscarcurso(curso.codigocurso):
            return False
        idx = self.__posicao_insercao(curso.codigocurso)
        self.cursos.insert(idx, curso)
        return True

    def buscarcurso(self, codigocurso):
        idx = self.__posicao_insercao(codigocurso)
        if idx < len(self.cursos) and self.cursos[idx].codigocurso == codigocurso:
            return self.cursos[idx]
        return None

    def removercurso(self, codigocurso):
        idx = self.__posicao_insercao(codigocurso)
        if idx < len(self.cursos) and self.cursos[idx].codigocurso == codigocurso:
            del self.cursos[idx]
            return True
        return False

    def listarcursos(self):
        return self.cursos

    def carregar_de_txt(self, caminho, limpar_antes=True):
        if limpar_antes:
            self.cursos = []
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                for linha in f:
                    dados = linha.strip().split('|')
                    if len(dados) == 2:
                        self.adicionarcurso(Curso(*dados))
        except FileNotFoundError:
            pass

    def salvar_para_txt(self, caminho):
        with open(caminho, 'w', encoding='utf-8') as f:
            for c in self.cursos:
                f.write(f"{c.codigocurso}|{c.nomecurso}\n")
