from autores.repository import AutoresDB
from autores.model import Autor

class AutorController:
    def __init__(self, db_autores: AutoresDB, cidade_controller):
        self.db = db_autores
        self.cidade_controller = cidade_controller  # Para validar cidades

    def adicionar_autor(self, nome, cod_cidade):
        if not self.cidade_controller.buscar_cidade(int(cod_cidade)):
            return False, "Código de cidade inválido."

        codigo = self.db.novo_codigo()
        autor = Autor(codigo, nome, cod_cidade)
        sucesso = self.db.adicionar_autor(autor)
        return sucesso, f"Autor adicionado com código {codigo}" if sucesso else "Erro ao adicionar autor."

    def listar_autores(self):
        return self.db.listar_autores()

    def buscar_autor(self, codigo):
        return self.db.buscar_autor(codigo)

    def remover_autor(self, codigo):
        return self.db.remover_autor(codigo)
