from cursos.model import Curso
from utils.busca import busca_binaria

class CursosDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.cursos = self.carregar_cursos()

    def carregar_cursos(self):
        cursos = []
        try:
            with open("txt/cursos.txt", "r") as f:
                for linha in f:
                    codigo, descricao = linha.strip().split("|")
                    cursos.append(Curso(int(codigo), descricao))
            if cursos:
                self.ultimo_codigo = cursos[-1].codigo
        except FileNotFoundError:
            pass
        return cursos

    def salvar_cursos(self):
        with open("txt/cursos.txt", "w") as f:
            for curso in self.cursos:
                f.write(f"{curso.codigo}|{curso.descricao}\n")

    def adicionar_curso(self, curso: Curso):
        if busca_binaria(self.cursos, curso.codigo) != -1:
            return False

        self.cursos.append(curso)
        self.ultimo_codigo = curso.codigo
        self.salvar_cursos()
        return True

    def buscar_curso(self, codigo):
        idx = busca_binaria(self.cursos, codigo)
        return self.cursos[idx] if idx != -1 else None

    def remover_curso(self, codigo):
        idx = busca_binaria(self.cursos, codigo)
        if idx == -1:
            return False
        del self.cursos[idx]
        self.salvar_cursos()
        return True

    def listar_cursos(self):
        return self.cursos[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo