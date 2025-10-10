import os

def garantir_diretorio():
    if not os.path.exists("txt"):
        os.makedirs("txt")

def salvar_em_arquivo(nome_arquivo, dados):
    caminho = f"txt/{nome_arquivo}.txt"
    with open(caminho, "w", encoding="utf-8") as f:
        for linha in dados:
            f.write(linha + "\n")

def seed_cidades():
    dados = [
        "1|Assis|SP",
        "2|Marília|SP",
        "3|Londrina|PR",
    ]
    salvar_em_arquivo("cidades", dados)

def seed_cursos():
    dados = [
        "1|Análise e Desenvolvimento de Sistemas",
        "2|Administração",
        "3|Direito",
    ]
    salvar_em_arquivo("cursos", dados)

def seed_categorias():
    dados = [
        "1|Romance",
        "2|Ficção Científica",
        "3|História",
        "4|Poesia",
    ]
    salvar_em_arquivo("categorias", dados)

def seed_autores():
    dados = [
        "1|Machado de Assis|1",
        "2|George Orwell|3",
        "3|Carlos Drummond de Andrade|1",
    ]
    salvar_em_arquivo("autores", dados)

def seed_alunos():
    dados = [
        "1|João da Silva|1|1",
        "2|Maria Souza|2|2",
        "3|Pedro Oliveira|1|3",
    ]
    salvar_em_arquivo("alunos", dados)

def seed_livros():
    dados = [
        "1|Dom Casmurro|1|1|1899|disponível",
        "2|1984|2|2|1949|disponível",
        "3|Alguma Poesia|3|4|1930|disponível",
    ]
    salvar_em_arquivo("livros", dados)

def executar_seed():
    garantir_diretorio()
    seed_cidades()
    seed_cursos()
    seed_categorias()
    seed_autores()
    seed_alunos()
    seed_livros()
    print("Seeder executado com sucesso!\n")

if __name__ == "__main__":
    executar_seed()
