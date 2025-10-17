from cidades.service import CidadeService

class CidadeController:
    def __init__(self, cidades_db):
        self.service = CidadeService(cidades_db)

    def adicionar_cidade(self):
        descricao = input("Descrição: ").strip()
        estado = input("Estado (UF): ").strip()
        sucesso, msg = self.service.adicionar_cidade(descricao, estado)
        print(msg)

    def listar_cidades(self):
        cidades = self.service.db.listar_cidades()
        if not cidades:
            print("Nenhuma cidade cadastrada.")
        else:
            for cidade in cidades:
                print(cidade)

    def buscar_cidade(self):
        sucesso, msg = self.service.buscar_cidade()
        print(msg)

    def remover_cidade(self):
        sucesso, msg = self.service.remover_cidade()
        print(msg)
