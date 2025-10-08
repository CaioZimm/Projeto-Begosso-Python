from cidades.service import CidadeService

class CidadeController:
    def __init__(self, db):
        self.service = CidadeService(db)

    def adicionar_cidade(self, descricao, estado):
        return self.service.adicionar_cidade(descricao, estado)

    def listar_cidades(self):
        return self.service.db.listar_cidades()

    def buscar_cidade(self, codigo):
        return self.service.db.buscar_cidade(codigo)

    def remover_cidade(self, codigo):
        return self.service.remover_cidade(codigo)