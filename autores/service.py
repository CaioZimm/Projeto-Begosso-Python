from autores.model import Autor
from autores.repository import AutoresDB
from cidades.repository import CidadesDB

class AutorService:
    def __init__(self, db: AutoresDB):
        self.db = db
        self.cidades_db = CidadesDB()

    # -------- Validação e criação --------
    def validar_dados(self, nome, cod_cidade):
        if not nome.strip():
            return False, "O nome do autor é obrigatório."

        if not self.cidades_db.listar_cidades():
            return False, "Precisa cadastrar uma cidade primeiro!"

        cidade = self.cidades_db.buscar_cidade(cod_cidade)
        if not cidade:
            return False, "Código de cidade inválido."

        return True, "Validação OK."

    def adicionar_autor(self, nome, cod_cidade):
        valido, msg = self.validar_dados(nome, cod_cidade)
        if not valido:
            return False, msg

        codigo = self.db.novo_codigo()
        autor = Autor(codigo, nome.strip(), cod_cidade)
        sucesso = self.db.adicionar_autor(autor)
        if sucesso:
            return True, f"Autor '{nome}' cadastrado com sucesso! (Código: {codigo})"
        return False, "Erro ao adicionar autor."

    def remover_autor(self, codigo):
        autor = self.db.buscar_autor(codigo)
        if not autor:
            return False, "Autor não encontrado."

        sucesso = self.db.remover_autor(codigo)
        if sucesso:
            return True, f"Autor '{autor.nome}' removido com sucesso!"
        return False, "Erro ao remover o autor."

    # -------- Consultas com Join --------
    def listar_autores_completo(self):
        autores = self.db.listar_autores()
        resultado = []
        for a in autores:
            cidade = self.cidades_db.buscar_cidade(a.cod_cidade)
            nome_cidade = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade não encontrada"

            resultado.append(
                f"{a.codigo} - {a.nome}\n   Cidade: {nome_cidade}"
            )
        return resultado

    def buscar_autor_completo(self, codigo):
        a = self.db.buscar_autor(codigo)
        if not a:
            return None
        cidade = self.cidades_db.buscar_cidade(a.cod_cidade)
        nome_cidade = f"{cidade.descricao} ({cidade.estado})" if cidade else "Cidade não encontrada"
        return f"{a.codigo} - {a.nome}\n   Cidade: {nome_cidade}"
