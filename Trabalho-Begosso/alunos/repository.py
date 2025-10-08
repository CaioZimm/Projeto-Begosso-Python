from alunos.model import Aluno
import bisect

class AlunosDB:
    def __init__(self):
        self.alunos = []
        self.cursos = {'1': 'Curso A', '2': 'Curso B'}
        self.cidades = {'1': 'Cidade X', '2': 'Cidade Y'}
        self.ultimo_codigo = 1000
    
    def adicionaraluno(self, aluno):
        index = bisect.bisect_left(self.alunos, aluno)
        if index < len(self.alunos) and self.alunos[index].codigo == aluno.codigo:
            return False
        self.alunos.insert(index, aluno)
        self.ultimo_codigo = aluno.codigo
        return True

    def buscaraluno(self, codigo: str):
        fake = Aluno(codigo, "", "", "")
        index = bisect.bisect_left(self.alunos, fake)
        if index < len(self.alunos) and self.alunos[index].codigo == codigo:
            return self.alunos[index]
        return None

    def removeraluno(self, codigo: str):
        aluno = self.buscaraluno(codigo)
        if aluno:
            self.alunos.remove(aluno)
            return True
        return False

    def listaralunos(self):
        return self.alunos[:]

    def listar_cursos(self):
        return self.cursos

    def listar_cidades(self):
        return self.cidades

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo