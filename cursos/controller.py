from cursos.service import CursoService

class CursoController:
    def __init__(self, cursos_db):
        self.service = CursoService(cursos_db)

    def adicionar_curso(self):
        descricao = input("Descrição do curso: ").strip()
        sucesso, msg = self.service.adicionar_curso(descricao)
        print(msg)

    def listar_cursos(self):
        cursos = self.service.db.listar_cursos()
        if not cursos:
            print("Nenhum curso cadastrado.")
        else:
            for curso in cursos:
                print(curso)

    def buscar_curso(self):
        sucesso, msg = self.service.buscar_curso()
        print(msg)

    def remover_curso(self):
        sucesso, msg = self.service.remover_curso()
        print(msg)