# Importando os menus
from alunos.menu import menu_alunos
from cursos.menu import menu_cursos
from autores.menu import menu_autores
from cidades.menu import menu_cidades

def menu():
    while True:
        print("---- Sistema de Biblioteca ----")
        print("1. Gerenciar Cidades")
        print("2. Gerenciar Cursos")
        print("3. Gerenciar Alunos")
        print("4. Gerenciar Autores")
        print("5. Gerenciar Categorias")
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
            print('sim\n')
            
        elif escolha == '0':
            print("Saindo...\n")
            break
        else:
            print("Opção inválida.")