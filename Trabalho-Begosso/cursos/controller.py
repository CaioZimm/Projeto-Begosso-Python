from cursos.service import CursoService

class CursoController:
    def __init__(self, db):
        self.service = CursoService(db)

    def adicionar_curso(self, descricao):
        return self.service.adicionar_curso(descricao)

    def listar_cursos(self):
        return self.service.db.listar_cursos()

    def buscar_curso(self, codigo):
        return self.service.db.buscar_curso(codigo)

    def remover_curso(self, codigo):
        return self.service.remover_curso(codigo)
