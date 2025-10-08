from cursos.model import Curso
from cursos.repository import CursosDB

class CursoService:
    def __init__(self, db: CursosDB):
        self.db = db

    def validar_curso(self, descricao):
        if not descricao or descricao.strip() == "":
            return False, "Descrição do curso é obrigatória."
        return True, "Validação OK."

    def adicionar_curso(self, descricao):
        valido, msg = self.validar_curso(descricao)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        curso = Curso(codigo, descricao.strip())
        sucesso = self.db.adicionar_curso(curso)
        if sucesso:
            return True, f"Curso {descricao} - código {codigo} adicionado com sucesso!"
        return False, "Erro: código duplicado."

    def remover_curso(self, codigo):
        curso = self.db.buscar_curso(codigo)
        if not curso:
            return False, "Curso não encontrado."

        sucesso = self.db.remover_curso(codigo)
        if sucesso:
            return True, f"Curso {curso.descricao} - {curso.codigo} removido com sucesso!"
        return False, "Erro ao remover o curso."
