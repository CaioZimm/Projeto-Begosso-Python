from alunos.repository import AlunosDB
from alunos.model import Aluno

class AlunoController:
    def __init__(self, db_alunos: AlunosDB):
        self.db = db_alunos

    def adicionar_aluno(self, nome, curso, cidade):
        codigo = self.db.novo_codigo()
        if self.db.buscaraluno(codigo):
            return False, "Código já existe."
        novo = Aluno(codigo, nome, curso, cidade)
        sucesso = self.db.adicionaraluno(novo)
        return sucesso, "Aluno adicionado com sucesso!" if sucesso else "Erro ao adicionar aluno."

    def listar_alunos(self):
        return self.db.listaralunos()

    def buscar_aluno(self, codigo):
        return self.db.buscaraluno(codigo)

    def remover_aluno(self, codigo):
        return self.db.removeraluno(codigo)

    def listar_cursos(self):
        return self.db.listar_cursos()

    def listar_cidades(self):
        return self.db.listar_cidades()