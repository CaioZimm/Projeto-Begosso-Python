from emprestimos.service import EmprestimoService

class EmprestimoController:
    def __init__(self, db):
        self.service = EmprestimoService(db)

    def realizar_emprestimo(self, cod_livro, cod_aluno):
        return self.service.realizar_emprestimo(cod_livro, cod_aluno)

    def devolver_livro(self, cod_emprestimo):
        return self.service.devolver_livro(cod_emprestimo)

    def listar_emprestimos(self):
        return self.service.listar_emprestimos_completo()

    def listar_atrasados(self):
        return self.service.listar_atrasados()
