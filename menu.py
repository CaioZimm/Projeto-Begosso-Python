# Importando os menus
from alunos.menu import menu_alunos
from cursos.menu import menu_cursos
from autores.menu import menu_autores
from cidades.menu import menu_cidades
from categorias.menu import menu_categorias
from livros.menu import menu_livros
from emprestimos.menu import menu_emprestimos
from utils.ui import limpar_tela

# Base de dados
from cidades.menu import menu_cidades
from cursos.menu import menu_cursos
from alunos.menu import menu_alunos
from autores.menu import menu_autores
from categorias.menu import menu_categorias
from livros.menu import menu_livros
from emprestimos.menu import menu_emprestimos

def menu(cidades_db, cursos_db, alunos_db, autores_db, categorias_db, livros_db, emprestimos_db):
    while True:
        limpar_tela()
        print("\n==== Sistema de Biblioteca ====\n")
        print("1 - Gerenciar Cidades")
        print("2 - Gerenciar Cursos")
        print("3 - Gerenciar Alunos")
        print("4 - Gerenciar Autores")
        print("5 - Gerenciar Categorias")
        print("6 - Gerenciar Livros")
        print("7 - Gerenciar Empréstimos")
        print("0 - Sair\n")

        escolha = input("Escolha: ").strip()
        if escolha == '1':
            menu_cidades(cidades_db)
        elif escolha == '2':
            menu_cursos(cursos_db)
        elif escolha == '3':
            menu_alunos(alunos_db, cursos_db, cidades_db)
        elif escolha == '4':
            menu_autores(autores_db, cidades_db)
        elif escolha == '5':
            menu_categorias(categorias_db)
        elif escolha == '6':
            menu_livros(livros_db, autores_db, categorias_db, cidades_db)
        elif escolha == '7':
            menu_emprestimos(emprestimos_db, livros_db, alunos_db)
            
        elif escolha == '0':
            print("Saindo...\n")
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")