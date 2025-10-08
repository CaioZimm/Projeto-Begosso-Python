from cursos.model import Curso

class CursosDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.cursos = self.carregar_cursos()

    def carregar_cursos(self):
        cursos = []
        try:
            with open("txt/cursos.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    codigo, descricao = linha.strip().split("|")
                    cursos.append(Curso(int(codigo), descricao))
            cursos.sort(key=lambda c: c.codigo)
            if cursos:
                self.ultimo_codigo = cursos[-1].codigo
        except FileNotFoundError:
            pass
        return cursos

    def salvar_cursos(self):
        with open("txt/cursos.txt", "w", encoding="utf-8") as f:
            for curso in self.cursos:
                f.write(f"{curso.codigo}|{curso.descricao}\n")

    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.cursos) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.cursos[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_curso(self, curso: Curso):
        if self._busca_binaria(curso.codigo) != -1:
            return False

        self.cursos.append(curso)
        self.cursos.sort(key=lambda c: c.codigo)
        self.ultimo_codigo = curso.codigo
        self.salvar_cursos()
        return True

    def buscar_curso(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.cursos[idx] if idx != -1 else None

    def remover_curso(self, codigo):
        idx = self._busca_binaria(codigo)
        if idx == -1:
            return False
        del self.cursos[idx]
        self.salvar_cursos()
        return True

    def listar_cursos(self):
        return self.cursos[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
