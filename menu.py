# Importando os menus
from alunos.menu import menu_alunos
from cursos.menu import menu_cursos
from autores.menu import menu_autores
from cidades.menu import menu_cidades
from categorias.menu import menu_categorias
from livros.menu import menu_livros
from emprestimos.menu import menu_emprestimos
from utils.ui import limpar_tela

def menu():
    while True:
        limpar_tela()
        print("\n---- Sistema de Biblioteca ----\n")
        print("1. Gerenciar Cidades")
        print("2. Gerenciar Cursos")
        print("3. Gerenciar Alunos")
        print("4. Gerenciar Autores")
        print("5. Gerenciar Categorias")
        print("6. Gerenciar Livros")
        print("7. Gerenciar Empréstimos")
        print("0. Sair\n")

        escolha = input("Escolha: ").strip()
        if escolha == '1':
            menu_cidades()
        elif escolha == '2':
            menu_cursos()
        elif escolha == '3':
            menu_alunos()
        elif escolha == '4':
            menu_autores()
        elif escolha == '5':
            menu_categorias()
        elif escolha == '6':
            menu_livros()
        elif escolha == '7':
            menu_emprestimos()
            
        elif escolha == '0':
            print("Saindo...\n")
            break
        else:
            print("Opção inválida.")