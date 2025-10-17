from menu import menu
from cidades.repository import CidadesDB
from cursos.repository import CursosDB
from alunos.repository import AlunosDB
from autores.repository import AutoresDB
from categorias.repository import CategoriasDB
from livros.repository import LivrosDB
from emprestimos.repository import EmprestimosDB

def main():
    cidades_db = CidadesDB()
    cursos_db = CursosDB()
    alunos_db = AlunosDB()
    autores_db = AutoresDB()
    categorias_db = CategoriasDB()
    livros_db = LivrosDB()
    emprestimos_db = EmprestimosDB()

    menu(cidades_db, cursos_db, alunos_db, autores_db, categorias_db, livros_db, emprestimos_db)

if __name__ == "__main__":
    main()
