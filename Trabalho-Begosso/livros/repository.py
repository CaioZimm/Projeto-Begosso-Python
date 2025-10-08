from livros.model import Livro

class LivrosDB:
    def __init__(self):
        self.ultimo_codigo = 0
        self.livros = self.carregar_livros()

    def carregar_livros(self):
        livros = []
        try:
            with open("txt/livros.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    codigo, titulo, cod_autor, cod_categoria, ano_publicacao, disponibilidade = linha.strip().split("|")
                    livros.append(Livro(int(codigo), titulo, int(cod_autor), int(cod_categoria), int(ano_publicacao), disponibilidade))
            livros.sort(key=lambda l: l.codigo)
            if livros:
                self.ultimo_codigo = livros[-1].codigo
        except FileNotFoundError:
            pass
        return livros

    def salvar_livros(self):
        with open("txt/livros.txt", "w", encoding="utf-8") as f:
            for livro in self.livros:
                f.write(f"{livro.codigo}|{livro.titulo}|{livro.cod_autor}|{livro.cod_categoria}|{livro.ano_publicacao}|{livro.disponibilidade}\n")

    def _busca_binaria(self, codigo):
        inicio, fim = 0, len(self.livros) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = self.livros[meio].codigo
            if atual == codigo:
                return meio
            elif atual < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

    def adicionar_livro(self, livro: Livro):
        if self._busca_binaria(livro.codigo) != -1:
            return False
        self.livros.append(livro)
        self.livros.sort(key=lambda l: l.codigo)
        self.ultimo_codigo = livro.codigo
        self.salvar_livros()
        return True

    def buscar_livro(self, codigo):
        idx = self._busca_binaria(codigo)
        return self.livros[idx] if idx != -1 else None

    def remover_livro(self, codigo):
        idx = self._busca_binaria(codigo)
        if idx == -1:
            return False
        del self.livros[idx]
        self.salvar_livros()
        return True

    def listar_livros(self):
        return self.livros[:]

    def novo_codigo(self):
        self.ultimo_codigo += 1
        return self.ultimo_codigo
