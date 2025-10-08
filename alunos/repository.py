from alunos.model import Aluno

class AlunosDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.alunos = self.carregar_alunos()

    def carregar_alunos(self):
        alunos = []
        try:
            with open("txt/alunos.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    codigo, nome, cod_curso, cod_cidade = linha.strip().split("|")
                    alunos.append(Aluno(int(codigo), nome, int(cod_curso), int(cod_cidade)))
            alunos.sort(key=lambda a: a.codigo)
            if alunos:
                self.ultimo_codigo = alunos[-1].codigo
        except FileNotFoundError:
            pass
        return alunos

    def salvar_alunos(self):
        with open("txt/alunos.txt", "w", encoding="utf-8") as f:
            for aluno in self.alunos:
                f.write(f"{aluno.codigo}|{aluno.nome}|{aluno.cod_curso}|{aluno.cod_cidade}\n")

    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.alunos) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.alunos[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_aluno(self, aluno: Aluno):
        if self._busca_binaria(aluno.codigo) != -1:
            return False

        self.alunos.append(aluno)
        self.alunos.sort(key=lambda a: a.codigo)
        self.ultimo_codigo = aluno.codigo
        self.salvar_alunos()
        return True

    def buscar_aluno(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.alunos[idx] if idx != -1 else None

    def remover_aluno(self, codigo):
        idx = self._busca_binaria(codigo)
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
