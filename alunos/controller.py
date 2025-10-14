from alunos.service import AlunoService
from cursos.repository import CursosDB
from cidades.repository import CidadesDB

class AlunoController:
    def __init__(self, db):
        self.service = AlunoService(db)
        self.cursos_db = CursosDB()
        self.cidades_db = CidadesDB()

    def adicionar_aluno(self):
        cursos = self.cursos_db.listar_cursos()
        cidades = self.cidades_db.listar_cidades()

        if not cursos or not cidades:
            print("Precisa cadastrar uma cidade e um curso primeiro!")
            return

        nome = input("Nome do aluno: ").strip()

        print("\n--- Cursos Disponíveis ---")
        for c in cursos:
            print(f"{c.codigo} - {c.descricao}")
        cod_curso = int(input("Código do curso: "))

        print("\n--- Cidades Disponíveis ---")
        for c in cidades:
            print(f"{c.codigo} - {c.descricao} ({c.estado})")
        cod_cidade = int(input("Código da cidade: "))

        sucesso, msg = self.service.adicionar_aluno(nome, cod_curso, cod_cidade)
        print(msg)

    def listar_alunos(self):
        alunos = self.service.listar_alunos_completo()
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for a in alunos:
                print(a)
                print("-" * 40)

    def buscar_aluno(self):
        sucesso, msg = self.service.buscar_aluno()
        print(msg)

    def remover_aluno(self):
        sucesso, msg = self.service.remover_aluno()
        print(msg)
