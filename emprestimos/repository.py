from emprestimos.model import Emprestimo

class EmprestimosDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.emprestimos = self.carregar_emprestimos()

    def carregar_emprestimos(self):
        emprestimos = []
        try:
            with open("txt/emprestimos.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    codigo, cod_livro, cod_aluno, data_emp, data_dev, devolvido = linha.strip().split("|")
                    emprestimos.append(Emprestimo(int(codigo), int(cod_livro), int(cod_aluno), data_emp, data_dev, devolvido))
            emprestimos.sort(key=lambda e: e.codigo)
            if emprestimos:
                self.ultimo_codigo = emprestimos[-1].codigo
        except FileNotFoundError:
            pass
        return emprestimos

    def salvar_emprestimos(self):
        with open("txt/emprestimos.txt", "w", encoding="utf-8") as f:
            for e in self.emprestimos:
                f.write(f"{e.codigo}|{e.cod_livro}|{e.cod_aluno}|{e.data_emprestimo}|{e.data_devolucao}|{e.devolvido}\n")

    # --- Busca binária ---
    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.emprestimos) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.emprestimos[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        if self._busca_binaria(emprestimo.codigo) != -1:
            return False
        self.emprestimos.append(emprestimo)
        self.emprestimos.sort(key=lambda e: e.codigo)
        self.ultimo_codigo = emprestimo.codigo
        self.salvar_emprestimos()
        return True

    def listar_emprestimos(self):
        return self.emprestimos[:]

    def buscar_emprestimo(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.emprestimos[idx] if idx != -1 else None

    def atualizar(self):
        self.salvar_emprestimos()

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
