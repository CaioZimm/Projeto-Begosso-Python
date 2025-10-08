from alunos.model import Aluno
from alunos.repository import AlunosDB
from cursos.repository import CursosDB
from cidades.repository import CidadesDB

class AlunoService:
    def __init__(self, db: AlunosDB):
        self.db = db
        self.cursos_db = CursosDB()
        self.cidades_db = CidadesDB()

    # ----------- Validação e criação -----------
    def validar_dados(self, nome, cod_curso, cod_cidade):
        if not nome.strip():
            return False, "O nome do aluno é obrigatório."

        if not self.cursos_db.listar_cursos() or not self.cidades_db.listar_cidades():
            return False, "Precisa cadastrar uma cidade e um curso primeiro!"

        curso = self.cursos_db.buscar_curso(cod_curso)
        cidade = self.cidades_db.buscar_cidade(cod_cidade)

        if not curso:
            return False, "Código de curso inválido."
        if not cidade:
            return False, "Código de cidade inválido."

        return True, "Validação OK."

    def adicionar_aluno(self, nome, cod_curso, cod_cidade):
        valido, msg = self.validar_dados(nome, cod_curso, cod_cidade)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        aluno = Aluno(codigo, nome.strip(), cod_curso, cod_cidade)
        sucesso = self.db.adicionar_aluno(aluno)
        if sucesso:
            return True, f"Aluno '{nome}' cadastrado com sucesso! (Código: {codigo})"
        return False, "Erro ao adicionar aluno."

    def remover_aluno(self, codigo):
        aluno = self.db.buscar_aluno(codigo)
        if not aluno:
            return False, "Aluno não encontrado."

        sucesso = self.db.remover_aluno(codigo)
        if sucesso:
            return True, f"Aluno '{aluno.nome}' removido com sucesso!"
        return False, "Erro ao remover o aluno."

    # ----------- Consultas com Join -----------
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
        a = self.db.buscar_aluno(codigo)
        if not a:
            return None
        curso = self.cursos_db.buscar_curso(a.cod_curso)
        cidade = self.cidades_db.buscar_cidade(a.cod_cidade)
        nome_curso = curso.descricao if curso else "Curso não encontrado"
        nome_cidade = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade não encontrada"
        return (
            f"{a.codigo} - {a.nome}\n   Curso: {nome_curso}\n   Cidade: {nome_cidade}"
        )