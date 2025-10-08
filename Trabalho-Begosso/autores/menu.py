from autores.repository import AutoresDB
from autores.controller import AutorController
from cidades.repository import CidadesDB
from cidades.controller import CidadeController

db_cidades = CidadesDB()
controller_cidades = CidadeController(db_cidades)
db_autores = AutoresDB()
controller_autores = AutorController(db_autores, controller_cidades)

def menu_autores():
    while True:
        print("\n--- Menu Autores ---")
        print("1. Adicionar Autor")
        print("2. Listar Autores")
        print("3. Buscar Autor")
        print("4. Remover Autor")
        print("0. Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            nome = input("Nome: ")

            cidades = controller_cidades.listar_cidades()
            if not cidades:
                print("Nenhuma cidade cadastrada. Cadastre uma cidade primeiro.")
                continue

            print("Cidades disponíveis:")
            for cidade in cidades:
                print(cidade)

            cod_cidade = input("Código da cidade: ")

            sucesso, msg = controller_autores.adicionar_autor(nome, cod_cidade)
            print(msg)

        elif opcao == "2":
            autores = controller_autores.listar_autores()
            for a in autores:
                print(a)

        elif opcao == "3":
            codigo = int(input("Código do autor: "))
            autor = controller_autores.buscar_autor(codigo)
            print(autor if autor else "Autor não encontrado.")

        elif opcao == "4":
            codigo = int(input("Código do autor: "))
            print("Removido!" if controller_autores.remover_autor(codigo) else "Autor não encontrado.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
