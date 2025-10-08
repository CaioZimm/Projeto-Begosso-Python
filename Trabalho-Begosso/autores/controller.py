from autores.service import AutorService

class AutorController:
    def __init__(self, db):
        self.service = AutorService(db)

    def adicionar_autor(self, nome, cod_cidade):
        return self.service.adicionar_autor(nome, cod_cidade)

    def listar_autores(self):
        return self.service.listar_autores_completo()

    def buscar_autor(self, codigo):
        return self.service.buscar_autor_completo(codigo)

    def remover_autor(self, codigo):
        return self.service.remover_autor(codigo)
