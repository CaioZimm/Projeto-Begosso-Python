from autores.repository import AutoresDB
from cidades.repository import CidadesDB
from autores.model import Autor
from utils.validation_input import ler_codigo

class AutorService:
    def __init__(self):
        self.db = AutoresDB()
        self.cidades_db = CidadesDB()

    def validar_dados(self, nome, cod_cidade):
        if not nome.strip():
            return False, "O nome do autor é obrigatório."

        cidade = self.cidades_db.buscar_cidade(cod_cidade)
        if not cidade:
            return False, "Código de cidade inválido."

        return True, "Validação correta"

    def adicionar_autor(self, nome, cod_cidade):
        valido, msg = self.validar_dados(nome, cod_cidade)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        autor = Autor(codigo, nome.strip(), cod_cidade)
        sucesso = self.db.adicionar_autor(autor)
        if sucesso:
            return True, f"Autor {nome} - código {codigo} cadastrado com sucesso!"
        return False, "Error"

    def listar_autores_completo(self):
        autores = self.db.listar_autores()
        resultado = []
        for a in autores:
            cidade = self.cidades_db.buscar_cidade(a.cod_cidade)
            nome_cidade = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade não encontrada"
            resultado.append(f"{a.codigo} - {a.nome}\n   Cidade: {nome_cidade}")
        return resultado

    def buscar_autor(self):
        sucesso, codigo = ler_codigo("Código do autor: ")
        if not sucesso:
            return False, codigo

        autor = self.db.buscar_autor(codigo)
        if autor:
            return True, str(autor)
        else:
            return False, "Autor não encontrado."

    def remover_autor(self):
        sucesso, codigo = ler_codigo("Código do autor: ")
        if not sucesso:
            return False, codigo
        
        autor = self.db.buscar_autor(codigo)
        if not autor:
            return False, "Autor não encontrado."

        sucesso = self.db.remover_autor(codigo)
        if sucesso:
            return True, f"Autor {autor.nome} - {autor.codigo} removido com sucesso!"
        return False, "Error"
