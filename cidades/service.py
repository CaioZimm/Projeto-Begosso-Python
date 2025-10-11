from cidades.model import Cidade
from cidades.repository import CidadesDB
from utils.validation_input import ler_codigo

class CidadeService:
    def __init__(self, db: CidadesDB):
        self.db = db

    def validar_cidade(self, descricao, estado):
        if not descricao or not estado:
            return False, "Descrição e Estado são obrigatórios."
        if len(estado.strip()) != 2:
            return False, "Estado (UF) deve conter apenas 2 letras."
        return True, "Validação correta"

    def adicionar_cidade(self, descricao, estado):
        valido, msg = self.validar_cidade(descricao, estado)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        cidade = Cidade(codigo, descricao.strip(), estado.strip().upper())
        sucesso = self.db.adicionar_cidade(cidade)
        if sucesso:
            return True, f"Cidade {descricao} - código {codigo} adicionada com sucesso!"
        return False, "Erro ao adicionar cidade."

    def buscar_cidade(self):
        sucesso, codigo = ler_codigo()
        if not sucesso:
            return False, codigo

        cidade = self.db.buscar_cidade(codigo)
        if cidade:
            return True, str(cidade)
        else:
            return False, "Cidade não encontrada."

    def remover_cidade(self):
        sucesso, codigo = ler_codigo()
        if not sucesso:
            return False, codigo

        cidade = self.db.buscar_cidade(codigo)
        if not cidade:
            return False, "Cidade não encontrada."

        sucesso = self.db.remover_cidade(codigo)
        if sucesso:
            return True, f"Cidade {cidade.descricao} - {cidade.codigo} removida com sucesso!"
        return False, "Erro ao remover cidade."