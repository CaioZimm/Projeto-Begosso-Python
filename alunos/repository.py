from alunos.model import Aluno
from utils.busca import busca_binaria

class AlunosDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.alunos = self.carregar_alunos()

    def carregar_alunos(self):
        alunos = []
        try:
            with open("txt/alunos.txt", "r") as f:
                for linha in f:
                    codigo, nome, cod_curso, cod_cidade = linha.strip().split("|")
                    alunos.append(Aluno(int(codigo), nome, int(cod_curso), int(cod_cidade)))
            if alunos:
                self.ultimo_codigo = alunos[-1].codigo
        except FileNotFoundError:
            pass
        return alunos

    def salvar_alunos(self):
        with open("txt/alunos.txt", "w") as f:
            for aluno in self.alunos:
                f.write(f"{aluno.codigo}|{aluno.nome}|{aluno.cod_curso}|{aluno.cod_cidade}\n")

    def adicionar_aluno(self, aluno: Aluno):
        if busca_binaria(self.alunos, aluno.codigo) != -1:
            return False

        self.alunos.append(aluno)
        self.ultimo_codigo = aluno.codigo
        self.salvar_alunos()
        return True

    def buscar_aluno(self, codigo):
        idx = busca_binaria(self.alunos, codigo)
        return self.alunos[idx] if idx != -1 else None

    def remover_aluno(self, codigo):
        idx = busca_binaria(self.alunos, codigo)
        if idx == -1:
            return False
        del self.alunos[idx]
        self.salvar_alunos()
        return True

    def listar_alunos(self):
        return self.alunos[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
