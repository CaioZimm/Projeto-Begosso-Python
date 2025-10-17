from alunos.model import Aluno
from utils.validation_input import ler_codigo

class AlunoService:
    def __init__(self, alunos_db, cursos_db, cidades_db):
        self.db = alunos_db
        self.cursos_db = cursos_db
        self.cidades_db = cidades_db

    def validar_dados(self, nome, cod_curso, cod_cidade):
        if not nome.strip():
            return False, "O nome do aluno é obrigatório."

        curso = self.cursos_db.buscar_curso(cod_curso)
        cidade = self.cidades_db.buscar_cidade(cod_cidade)

        if not curso:
            return False, "Código de curso inválido."
        if not cidade:
            return False, "Código de cidade inválido."

        return True, "Validação correta"

    def adicionar_aluno(self, nome, cod_curso, cod_cidade):
        valido, msg = self.validar_dados(nome, cod_curso, cod_cidade)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        aluno = Aluno(codigo, nome.strip(), cod_curso, cod_cidade)
        sucesso = self.db.adicionar_aluno(aluno)

        if sucesso:
            return True, f"Aluno {nome} - código {codigo} cadastrado com sucesso!"
        return False, "Error"

    def listar_alunos_completo(self):
        alunos = self.db.listar_alunos()
        resultado = []
        for a in alunos:
            curso = self.cursos_db.buscar_curso(a.cod_curso)
            cidade = self.cidades_db.buscar_cidade(a.cod_cidade)
            nome_curso = curso.descricao if curso else "Curso não encontrado"
            nome_cidade = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade não encontrada"

            resultado.append(
                f"{a.codigo} - {a.nome}\n   Curso: {nome_curso}\n   Cidade: {nome_cidade}"
            )
        return resultado

    def buscar_aluno_completo(self, codigo):
        aluno = self.db.buscar_aluno(codigo)
        if not aluno:
            return None
        curso = self.cursos_db.buscar_curso(aluno.cod_curso)
        cidade = self.cidades_db.buscar_cidade(aluno.cod_cidade)
        nome_curso = curso.descricao if curso else "Curso não encontrado"
        nome_cidade = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade não encontrada"
        return (
            f"{aluno.codigo} - {aluno.nome}\n   Curso: {nome_curso}\n   Cidade: {nome_cidade}"
        )
    
    def buscar_aluno(self):
        sucesso, codigo = ler_codigo("Código do aluno: ")
        if not sucesso:
            return False, codigo

        aluno = self.db.buscar_aluno(codigo)
        if aluno:
            return True, str(aluno)
        else:
            return False, "Aluno não encontrado."

    def remover_aluno(self):
        sucesso, codigo = ler_codigo("Código do aluno: ")
        if not sucesso:
            return False, codigo

        aluno = self.db.buscar_aluno(codigo)
        if not aluno:
            return False, "Aluno não encontrado."

        sucesso = self.db.remover_aluno(codigo)
        if sucesso:
            return True, f"Aluno {aluno.nome} - {aluno.codigo} removido com sucesso!"
        return False, "Erro ao remover o aluno."
