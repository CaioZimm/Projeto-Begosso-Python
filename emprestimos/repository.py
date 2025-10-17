from emprestimos.model import Emprestimo
from utils.busca import busca_binaria

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
            if emprestimos:
                self.ultimo_codigo = emprestimos[-1].codigo
        except FileNotFoundError:
            pass
        return emprestimos

    def salvar_emprestimos(self):
        with open("txt/emprestimos.txt", "w", encoding="utf-8") as f:
            for e in self.emprestimos:
                f.write(f"{e.codigo}|{e.cod_livro}|{e.cod_aluno}|{e.data_emprestimo}|{e.data_devolucao}|{e.devolvido}\n")

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        if busca_binaria(self.emprestimos, emprestimo.codigo) != -1:
            return False
        
        self.emprestimos.append(emprestimo)
        self.ultimo_codigo = emprestimo.codigo

        self.salvar_emprestimos()
        return True

    def listar_emprestimos(self):
        return self.emprestimos[:]

    def buscar_emprestimo(self, codigo):
        index = busca_binaria(self.emprestimos, codigo)
        return self.emprestimos[index] if index != -1 else None

    def atualizar(self):
        self.salvar_emprestimos()

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
