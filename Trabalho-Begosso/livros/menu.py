from livros.repository import LivrosDB
from livros.controller import LivroController
from autores.repository import AutoresDB
from categorias.repository import CategoriasDB
from cidades.repository import CidadesDB
from utils.ui import limpar_tela

db = LivrosDB()
controller = LivroController(db)
autores_db = AutoresDB()
categorias_db = CategoriasDB()
cidades_db = CidadesDB()

def menu_livros():
    while True:
        limpar_tela()
        print("\n--- Menu Livros ---\n")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Remover Livro")
        print("0. Voltar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            autores = autores_db.listar_autores()
            categorias = categorias_db.listar_categorias()

            if not autores or not categorias:
                print("Precisa cadastrar um autor e uma categoria primeiro!")
                input("\nPressione Enter para continuar...")
                continue

            print("\n--- Autores Disponíveis ---")
            for a in autores:
                cidade = cidades_db.buscar_cidade(a.cod_cidade)
                print(f"{a.codigo} - {a.nome} ({cidade.descricao} - {cidade.estado})" if cidade else f"{a.codigo} - {a.nome}")

            print("\n--- Categorias Disponíveis ---")
            for c in categorias:
                print(f"{c.codigo} - {c.descricao}")

            try:
                titulo = input("\nTítulo do livro: ").strip()
                cod_autor = int(input("Código do autor: "))
                cod_categoria = int(input("Código da categoria: "))
                ano_publicacao = int(input("Ano de publicação: "))

                sucesso, msg = controller.adicionar_livro(titulo, cod_autor, cod_categoria, ano_publicacao)
                print(msg)
            except ValueError:
                print("Código ou ano inválido!")
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            livros = controller.listar_livros()
            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                for l in livros:
                    print(l)
                    print("-" * 50)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            try:
                codigo = int(input("Código do livro: "))
                livro = controller.buscar_livro(codigo)
                print(livro if livro else "Livro não encontrado.")
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            try:
                codigo = int(input("Código do livro: "))
                sucesso, msg = controller.remover_livro(codigo)
                print(msg)
            except ValueError:
                print("Código inválido.")
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")
