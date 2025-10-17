from cursos.model import Curso
from cursos.repository import CursosDB
from utils.validation_input import ler_codigo

class CursoService:
    def __init__(self, cursos_db: CursosDB):
        self.db = cursos_db

    def validar_curso(self, descricao):
        if not descricao:
            return False, "Descrição do curso é obrigatória."
        return True, "Validação correta"

    def adicionar_curso(self, descricao):
        valido, msg = self.validar_curso(descricao)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        curso = Curso(codigo, descricao.strip())
        sucesso = self.db.adicionar_curso(curso)

        if sucesso:
            return True, f"Curso {descricao} - código {codigo} adicionado com sucesso!"
        return False, "Error"

    def buscar_curso(self):
        sucesso, codigo = ler_codigo("Código do curso: ")
        if not sucesso:
            return False, codigo

        curso = self.db.buscar_curso(codigo)
        if curso:
            return True, str(curso)
        else:
            return False, "Curso não encontrado."

    def remover_curso(self):
        sucesso, codigo = ler_codigo("Código do curso: ")
        if not sucesso:
            return False, codigo

        curso = self.db.buscar_curso(codigo)
        if not curso:
            return False, "Curso não encontrado."

        sucesso = self.db.remover_curso(codigo)
        if sucesso:
            return True, f"Curso {curso.descricao} - {curso.codigo} removido com sucesso!"
        return False, "Erro ao remover o curso."
