from cursos.model import Curso
from cursos.repository import CursosDB

class CursoController:
    def __init__(self, db: CursosDB):
        self.db = db

    def adicionar_curso(self, cod, nome):
        if self.db.buscarcurso(cod):
            return False, "Código já existe."
        curso = Curso(cod, nome)
        sucesso = self.db.adicionarcurso(curso)
        return sucesso, "Curso adicionado com sucesso!" if sucesso else "Erro ao adicionar curso."

    def listar_cursos(self):
        return self.db.listarcursos()

    def buscar_curso(self, cod):
        return self.db.buscarcurso(cod)

    def remover_curso(self, cod):
        return self.db.removercurso(cod)
