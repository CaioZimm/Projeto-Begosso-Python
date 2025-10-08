from alunos.service import AlunoService

class AlunoController:
    def __init__(self, db):
        self.service = AlunoService(db)

    def adicionar_aluno(self, nome, cod_curso, cod_cidade):
        return self.service.adicionar_aluno(nome, cod_curso, cod_cidade)

    def listar_alunos(self):
        return self.service.listar_alunos_completo()

    def buscar_aluno(self, codigo):
        return self.service.buscar_aluno_completo(codigo)

    def remover_aluno(self, codigo):
        return self.service.remover_aluno(codigo)
