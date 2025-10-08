from cidades.model import Cidade
from cidades.repository import CidadesDB

class CidadeService:
    def __init__(self, db: CidadesDB):
        self.db = db

    def validar_cidade(self, descricao, estado):
        if not descricao or not estado:
            return False, "Descrição e Estado são obrigatórios."
        return True, "Validação bem-sucedida"

    def adicionar_cidade(self, descricao, estado):
        valido, msg = self.validar_cidade(descricao, estado)
        if not valido:
            return False, msg

        cidade = Cidade(self.db.novo_codigo(), descricao, estado)
        return self.db.adicionar_cidade(cidade), f"Cidade de '{descricao}' com código {self.db.novo_codigo()} adicionada com sucesso!"
    
    def remover_cidade(self, codigo):
        cidade = self.db.buscar_cidade(codigo)
        if not cidade:
            return False, "Cidade não encontrada."

        sucesso = self.db.remover_cidade(codigo)
        if sucesso:
            return True, f"Cidade '{cidade.descricao}' removida com sucesso!"
        else:
            return False, "Erro ao remover a cidade."
