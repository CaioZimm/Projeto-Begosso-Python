from autores.service import AutorService
from cidades.repository import CidadesDB

class AutorController:
    def __init__(self):
        self.service = AutorService()
        self.cidades_db = CidadesDB()

    def adicionar_autor(self):
        cidades = self.cidades_db.listar_cidades()

        if not cidades:
            print("Precisa cadastrar uma cidade primeiro!")
            input("\nPressione Enter para continuar...")
            return

        nome = input("\nNome do autor: ").strip()

        print("\n--- Cidades Disponíveis ---")
        for c in cidades:
            print(f"{c.codigo} - {c.descricao} ({c.estado})")
        cod_cidade = int(input("Código da cidade: "))
       
        sucesso, msg = self.service.adicionar_autor(nome, cod_cidade)
        print(msg)

    def listar_autores(self):
        autores = self.service.listar_autores_completo()
        if not autores:
            print("Nenhum autor cadastrado.")
        else:
            for a in autores:
                print(a)
                print("-" * 40)

    def buscar_autor(self):
        sucesso, msg = self.service.buscar_autor()
        print(msg)

    def remover_autor(self):
        sucesso, msg = self.service.remover_autor()
        print(msg)